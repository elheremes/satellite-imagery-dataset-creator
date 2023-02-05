from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea
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


class MainWindow(QWidget):
    """
    Tela principal da interface do programa.
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.raster1_name = None
        self.raster2_name = None

        self.settings()
        self.create_widgets()
        self.set_layout()
        self.add_widgets()

        # self.data_controller = DataController()
        self.process_controller = ProcessController()

        self.load_processed_videos()

    def settings(self):
        self.resize(1200, 500)
        self.setWindowTitle("Raster GAN Dataset Creator")

    def create_widgets(self):
        # Butões
        self.btn_load_video_1 = QPushButton("Carregar Raster 1")
        self.btn_load_video_1.setObjectName("loadVideoButton")
        self.btn_load_video_1.setFixedWidth(200)
        self.btn_load_video_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_load_video_2 = QPushButton("Carregar Raster 2")
        self.btn_load_video_2.setObjectName("loadVideoButton")
        self.btn_load_video_2.setFixedWidth(200)
        self.btn_load_video_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_process = QPushButton("Adicionar a Fila")
        self.btn_process.setObjectName("processVideoButton")
        self.btn_process.setFixedWidth(200)
        self.btn_process.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_process.setDisabled(True)

        # Sinais
        self.btn_load_video_1.clicked.connect(self.add_raster_1)
        self.btn_load_video_2.clicked.connect(self.add_raster_2)
        self.btn_process.clicked.connect(self.add_process_to_queue)

    def set_layout(self):
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
        self.buttons_layout.addWidget(self.btn_load_video_1)
        self.buttons_layout.addWidget(self.btn_load_video_2)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.btn_process)

    def add_raster_1(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Selecione um raster", filter="TIFF(*.tiff *.tif)")

        if filename == '':
            return

        self.raster1_name = filename

        self.check_process_button()

    def add_raster_2(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Selecione um raster", filter="TIFF(*.tiff *.tif)")

        if filename == '':
            return

        self.raster2_name = filename

        self.check_process_button()

    def check_process_button(self):
        if self.raster1_name is not None:
            if self.raster2_name is not None:
                self.btn_process.setDisabled(False)

    def add_process_to_queue(self):
        process = ProcessingItem(
            raster1_name=self.raster1_name, raster2_name=self.raster2_name, folder='tmp', delete_event=None)

        self.raster1_name = None
        self.raster2_name = None

        self.btn_process.setDisabled(True)

        self.process_layout.addWidget(process)
        self.process_controller.append_to_queue(process)

    def load_processed_videos(self):
        pass

    # def add_new_video(self):
    #     filename, _ = QFileDialog.getOpenFileName(
    #         self, "Selecione um vídeo de cirurgia artroscópica", filter="VID(*.mpg *.mp4 *.mpeg *.mov *.wvm *.flv *.avi *.mkv)")
    #     if filename == '':
    #         return
    #     video = VideoItem(video_name=filename,
    #                       delete_event=self.data_controller.delete_data_file)
    #     self.videos_layout.addWidget(video)

    #     self.process_controller.append_to_queue(
    #         video)  # realiza a chamada de processamento

    # def load_processed_videos(self):
    #     videos = self.data_controller.load_data()
    #     for v in videos:
    #         video = VideoItem(
    #             video_name=v["name"], delete_event=self.data_controller.delete_data_file, processed=True, data=v)
    #         self.videos_layout.addWidget(video)
