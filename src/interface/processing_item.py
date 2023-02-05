"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Script responsável pela visualização do item de processamento
    na interface.

    Cada item de processamento mostra o status (%) do processamento
    e se já finalizado o acesso a pasta de resultados. Também permite
    a exclusão desse processo no histórico.
"""

import shutil

from showinfm import show_in_file_manager

from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QProgressBar,
    QGridLayout,
    QVBoxLayout,
    QFrame,
)

from PySide2.QtCore import (
    Qt,
    QSize
)

from PySide2.QtGui import (
    QCursor,
    QIcon
)


class ProcessingItem(QWidget):
    """
    Tela de item processado na interface.

    Informa os nomes dos rasters presentes no processo,
    progresso de processamento e atalhos para o usuário
    poder acessar os arquivos e deletar o resultado.

    [ATRIBUTOS]
        processed_status: booleano informando se o item já foi
                          processado ou não.
        raster1_name: caminho do primeiro raster.
        raster2_name: caminho do segundo raster.
        folder: caminho de salvamento dos dados gerados.
    """

    def __init__(self, raster1_name, raster2_name, folder, processed=False, parent=None):
        super(ProcessingItem, self).__init__(parent)

        self.processed_status = processed
        self.raster1_name = raster1_name
        self.raster2_name = raster2_name
        self.folder = folder

        self.create_widgets()
        self.set_layout()
        self.add_widgets()

        if processed:
            self.processed_video()

    def create_widgets(self):
        """
        Método responsável pela criação de botões, labels e
        sinais presentes na interface do item de processamento.
        """

        # Labels
        name_1 = self.raster1_name.split('/')[-1]
        name_2 = self.raster2_name.split('/')[-1]

        self.raster1_name_label = QLabel('{}\n{}'.format(name_1, name_2))
        self.raster1_name_label.setObjectName("videoLabel")

        # Botões
        self.statistic_btn = QPushButton()
        self.statistic_btn.setIcon(QIcon("./resources/folder.png"))
        self.statistic_btn.setIconSize(QSize(20, 20))
        self.statistic_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.statistic_btn.setDisabled(True)
        self.statistic_btn.setFixedWidth(40)
        self.statistic_btn.setFixedHeight(40)
        self.statistic_btn.setObjectName("statisticButton")

        self.trash_btn = QPushButton()
        self.trash_btn.setIcon(QIcon("./resources/trash.png"))
        self.trash_btn.setIconSize(QSize(20, 20))
        self.trash_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.trash_btn.setFixedWidth(40)
        self.trash_btn.setFixedHeight(40)
        self.trash_btn.setObjectName("trashButton")

        self.progress_bar = QProgressBar()
        self.progress_bar.hide()

        # Sinais
        self.trash_btn.clicked.connect(self.delete_element)
        self.statistic_btn.clicked.connect(self.open_results)

    def set_layout(self):
        """
        Método responsável por definir o formato do layout
        do item de processamento.
        """

        container = QFrame()
        container.setObjectName("videoContainer")

        self.video_layout = QGridLayout()
        container.setLayout(self.video_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container)
        main_layout.setMargin(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(main_layout)

    def add_widgets(self):
        """
        Responsável por ligar os botões, sinais e caixas de
        texto ao layout do item de processamento.
        """

        self.video_layout.addWidget(self.raster1_name_label, 0, 0)
        self.video_layout.addWidget(self.progress_bar, 0, 1)
        self.video_layout.addWidget(self.statistic_btn, 0, 3)
        self.video_layout.addWidget(self.trash_btn, 0, 4)

    def delete_element(self):
        """
        Deleta os arquivos em discos relacionado ao processo e
        o exclui da interface.
        """

        shutil.rmtree(self.folder)

        self.setParent(None)

    def processed_video(self):
        """
        Habilita o botão para acessar os dados do resultado em
        disco.
        """

        self.statistic_btn.setDisabled(False)

    def open_results(self):
        """
        Abre os resultados no diretório do sistema.
        """

        show_in_file_manager(self.folder)

    def start_processing(self):
        """
        Habilita a barra de progresso do processamento.
        """

        self.progress_bar.setValue(0)
        self.progress_bar.show()

    def end_processing(self, data):
        """
        Desabilita a barra de progresso do processamento.
        """

        self.progress_bar.hide()
        self.statistic_btn.setDisabled(False)

    def update_progress(self, value):
        """
        Atualiza o valor da barra de progresso do processamento.

        [ARGUMENTOS]
            value: inteiro que representa a porcentagem da
                   barra de progresso.
        """

        self.progress_bar.setValue(value)

    def enable_trash_btn(self):
        """
        Habilita o botão de exclusão do elemento.
        """

        self.trash_btn.setDisabled(False)

    def disable_trash_btn(self):
        """
        Desabilita o botão de exclusão do elemento.
        """

        self.trash_btn.setDisabled(True)
