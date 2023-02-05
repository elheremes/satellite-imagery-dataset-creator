"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Script responsável pela criação da tela principal do programa.

    A tela é responsável pelo carregamento dos rasters, visualização
    da fila e do status dos processos e acesso aos resultados.
"""

from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QLabel
)

from PySide2.QtCore import (
    Qt
)

from PySide2.QtGui import (
    QCursor
)

from src.interface import (
    ProcessingItem
)

from src.controller import (
    ProcessController
)

from src.imgproc import (
    get_list_of_process_ids,
    get_new_id
)


class MainWindow(QWidget):
    """
    Tela principal da interface do programa.

    Recebe a upload dos rasters e mostra a fila de processamento
    e histórico de resultados.

    [ATRIBUTOS]
        raster1_name: caminho do primeiro raster enviado.
        raster2_name: caminho do segundo raster enviado.
        process_controller: Classe ProcessController responsável
                            pela execução do backend.
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.raster1_name = None
        self.raster2_name = None

        self.settings()
        self.create_widgets()
        self.set_layout()
        self.add_widgets()

        self.process_controller = ProcessController()

        self.load_processed_videos()

    def settings(self):
        """
        Definição de configurações básicas do Qt, como
        tamanho e título da janela.
        """

        self.resize(1200, 500)
        self.setWindowTitle("Raster GAN Dataset Creator")

    def create_widgets(self):
        """
        Método responsável pela criação de botões, labels e
        sinais presentes na interface da janela principal.
        """

        # Botões
        self.btn_load_video_1 = QPushButton("Carregar Raster 1")
        self.btn_load_video_1.setObjectName("loadVideoButton")
        self.btn_load_video_1.setFixedWidth(200)
        self.btn_load_video_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_load_video_2 = QPushButton("Carregar Raster 2")
        self.btn_load_video_2.setObjectName("loadVideoButton")
        self.btn_load_video_2.setFixedWidth(200)
        self.btn_load_video_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_process = QPushButton("Adicionar à Fila")
        self.btn_process.setObjectName("processVideoButton")
        self.btn_process.setFixedWidth(200)
        self.btn_process.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_process.setDisabled(True)

        # Labels
        self.raster1_label = QLabel('')
        self.raster1_label.setObjectName("regionLabel")
        self.raster1_label.setAlignment(Qt.AlignCenter)
        self.raster1_label.setDisabled(True)

        self.raster2_label = QLabel('')
        self.raster2_label.setObjectName("regionLabel")
        self.raster2_label.setAlignment(Qt.AlignCenter)
        self.raster2_label.setDisabled(True)

        # Sinais
        self.btn_load_video_1.clicked.connect(self.add_raster_1)
        self.btn_load_video_2.clicked.connect(self.add_raster_2)
        self.btn_process.clicked.connect(self.add_process_to_queue)

    def set_layout(self):
        """
        Método responsável por definir o formato do layout
        da janela principal.
        """

        self.scroll = QScrollArea()
        self.scroll.setObjectName("videosContainer")
        self.widget = QWidget()

        self.process_layout = QVBoxLayout()
        self.process_layout.setMargin(0)
        self.process_layout.setSpacing(0)
        self.process_layout.setContentsMargins(0, 0, 0, 0)
        self.process_layout.setAlignment(Qt.AlignTop)

        self.widget.setLayout(self.process_layout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setAlignment(Qt.AlignTop)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.scroll)
        main_layout.addLayout(self.buttons_layout)

        self.setLayout(main_layout)

    def add_widgets(self):
        """
        Responsável por ligar os botões, sinais e caixas de
        texto ao layout da tela principal.
        """

        self.buttons_layout.addWidget(self.btn_load_video_1)
        self.buttons_layout.addWidget(self.raster1_label)
        self.buttons_layout.addWidget(self.btn_load_video_2)
        self.buttons_layout.addWidget(self.raster2_label)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.btn_process)

    def add_raster_1(self):
        """
        Obtém o caminho em arquivo do primeiro raster informado
        pelo usuário ao pressionar o botão.
        """

        filename, _ = QFileDialog.getOpenFileName(
            self, "Selecione um raster", filter="TIFF(*.tiff *.tif)")

        if filename == '':
            return

        self.raster1_name = filename

        self.raster1_label.setText(filename.split('/')[-1])
        self.raster1_label.setDisabled(False)

        self.check_process_button()

    def add_raster_2(self):
        """
        Obtém o caminho em arquivo do segundo raster informado
        pelo usuário ao pressionar o botão.
        """

        filename, _ = QFileDialog.getOpenFileName(
            self, "Selecione um raster", filter="TIFF(*.tiff *.tif)")

        if filename == '':
            return

        self.raster2_name = filename

        self.raster2_label.setText(filename.split('/')[-1])
        self.raster2_label.setDisabled(False)

        self.check_process_button()

    def check_process_button(self):
        """
        Verifica se ambos os rasters já foram informados e habilita
        o botão de enviar a fila caso verdadeiro.
        """

        if self.raster1_name is not None:
            if self.raster2_name is not None:
                self.btn_process.setDisabled(False)

    def add_process_to_queue(self):
        """
        Cria um objeto de processo e envia para a fila de processamento.
        Além disso, limpa os dados de upload na interface e bloqueia o botão
        de envio para fila para evitar duplicações acidentais pelo usuário.
        """

        process_id = get_new_id()

        process = ProcessingItem(
            raster1_name=self.raster1_name, raster2_name=self.raster2_name,
            folder='tmp/{}'.format(process_id))

        self.raster1_name = None
        self.raster2_name = None

        self.raster1_label.setText('')
        self.raster1_label.setDisabled(True)
        self.raster2_label.setText('')
        self.raster2_label.setDisabled(True)

        self.btn_process.setDisabled(True)

        self.process_layout.addWidget(process)
        self.process_controller.append_to_queue(process)

    def load_processed_videos(self):
        """
        Carrega o histórico de execuções presentes nos arquivos e os manda
        para interface.
        """

        ids = get_list_of_process_ids()

        for i in ids:
            with open('tmp/{}/names.txt'.format(i), 'r') as f:
                raster1_name = f.readline()[:-1]
                raster2_name = f.readline()[:-1]

            p = ProcessingItem(raster1_name=raster1_name, raster2_name=raster2_name,
                               folder='tmp/{}'.format(i), processed=True)

            self.process_layout.addWidget(p)
