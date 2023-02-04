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

# from src.interface import (
#     VideoItem
# )

# from src.controller import (
#     VideoProcessController,
#     DataController
# )


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.settings()
        self.create_widgets()
        self.set_layout()
        self.add_widgets()

        # self.data_controller = DataController()
        # self.process_controller = VideoProcessController()

        self.load_processed_videos()

    def settings(self):
        self.resize(1200, 500)
        self.setWindowTitle("Raster GAN Dataset Creator")

    def create_widgets(self):
        # Butões
        self.btn_load_video = QPushButton("Carregar Vídeo")
        # define nome especificos para o objeto com o intuito de personalizar a interface
        self.btn_load_video.setObjectName("loadVideoButton")
        self.btn_load_video.setFixedWidth(200)
        self.btn_load_video.setCursor(QCursor(Qt.PointingHandCursor))

        # Sinais
        self.btn_load_video.clicked.connect(self.add_new_video)

    def set_layout(self):
        self.scroll = QScrollArea()
        self.scroll.setObjectName("videosContainer")
        self.widget = QWidget()

        self.videos_layout = QVBoxLayout()
        self.videos_layout.setMargin(0)
        self.videos_layout.setSpacing(0)
        self.videos_layout.setContentsMargins(0, 0, 0, 0)
        self.videos_layout.setAlignment(Qt.AlignTop)

        self.widget.setLayout(self.videos_layout)
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
        self.buttons_layout.addWidget(self.btn_load_video)

    def add_new_video(self):
        pass

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
