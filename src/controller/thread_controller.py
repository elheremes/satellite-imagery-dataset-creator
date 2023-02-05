"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Controlador responsável pela definição das classes
    de Threads na padronização do QT PySide2.
"""

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

    Finalizado [finished]: sem dados.
    Error [error]: tupla (exctype, valor, traceback.format_exc()).
    Resultado [result]: objeto de dados retornado do processamento,
                        qualquer coisa.
    Progresso [progress]: inteiro indicando % de progresso.
    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    """
    Thread do Worker;
    Herda de QRunnable para lidar com a configuração de threads de trabalho,
    sinais e conclusão.

    [ATRIBUTOS]
        fn: função de retorno a ser executada na thread de trabalho.
        args: argumentos para passa para a função de retorno.
        kwargs: palavras-chave para passar para função de retorno.
        signals: classe WorkerSignals para uso de sinais.
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        """
        Inicializa a execução da função informada passando os
        argumentos e palavras-chave.

        Ao final emite um sinal para o programa principal
        informando o status da thread.
        """

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
