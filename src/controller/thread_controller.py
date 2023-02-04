from PySide2.QtCore import (
    QObject,
    QRunnable,
    Signal,
    Slot
)

import traceback
import sys


class WorkerSignals(QObject):
    """
    Define os sinais disponíveis de um thread de trabalho em execução.
    Os sinais suportados são:
    finalizado
        Sem dados
    erro
        tupla (exctype, valor, traceback.format_exc() )
    resultado
        objeto de dados retornado do processamento, qualquer coisa
    progresso
        inteiro indicando % de progresso
    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    """
    Thread do Worker
    Herda de QRunnable para lidar com a configuração de threads de trabalho, sinais e conclusão.
    :param callback: A função de retorno a ser executada neste thread de trabalho. Os argumentos fornecidos e
                     kwargs serão passados para o runner.
    :type callback: função
    :param args: Argumentos para passar para a função de retorno
    :param kwargs: Palavras-chave para passar para a função de retorno

    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()  # Done
