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

    def __init__(self, delete_event, parent=None, raster1_name=None, raster2_name=None, processed=False, data={}):
        super(ProcessingItem, self).__init__(parent)

        self.delete_event = delete_event
        self.processed_status = processed
        self.raster1_name = raster1_name
        self.raster2_name = raster2_name
        self.processing_data = data

        self.create_widgets()
        self.set_layout()
        self.add_widgets()

        if processed:
            self.processed_video()

    def create_widgets(self):
        name = self.raster1_name.split('/')[-1]
        self.raster1_name_label = QLabel(name)
        self.raster1_name_label.setObjectName("videoLabel")

        name = self.raster2_name.split('/')[-1]
        self.raster2_name_label = QLabel(name)
        self.raster2_name_label.setObjectName("videoLabel")

        self.statistic_btn = QPushButton()
        self.statistic_btn.setIcon(QIcon("./resources/statistic.png"))
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

        # self.trash_btn.clicked.connect(self.delete_element)
        # self.statistic_btn.clicked.connect(self.open_results)

    def mousePressEvent(self, event):
        pass

        # if len(self.video_data) != 0:
        #     self.open_results()

    def set_layout(self):
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
        self.video_layout.addWidget(self.raster1_name_label, 0, 0)
        self.video_layout.addWidget(self.progress_bar, 0, 1)
        self.video_layout.addWidget(self.statistic_btn, 0, 3)
        self.video_layout.addWidget(self.trash_btn, 0, 4)

    def delete_element(self):
        pass
        # if len(self.video_data) != 0:
        #     self.delete_event(self.video_data["name"].split('/')[-1])
        # self.setParent(None)

    def processed_video(self):
        pass

        # self.statistic_btn.setDisabled(False)

    def set_data(self, data: dict):  # TODO: think in a Model
        pass

        # self.video_data = data

    def open_results(self):
        pass

        # self.results_window = ResultsWindow(self.video_data)
        # self.results_window.setWindowModality(Qt.ApplicationModal)
        # self.results_windo2w.show()

    def start_processing(self):
        self.progress_bar.setValue(0)
        self.progress_bar.show()

    def end_processing(self, data):
        self.progress_bar.hide()
        self.statistic_btn.setDisabled(False)
        # self.set_data(data)

    def update_progress(self, value):
        self.progress_bar.setValue(value)
