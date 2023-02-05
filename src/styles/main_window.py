'''
#015A63
#1EE6FC
#049FB0
#632A00
#B04D04
'''

stylesheet = """

QProgressBar {
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
    margin-right: 20px;
    margin-left: 20px;
}

QProgressBar::chunk {
    background-color: #049FB0;
    width: 20px;
}

QPushButton#loadVideoButton {
    background-color: #015A63;
    width: 70px;
    height: 50px;
    color: #FFF;
    font-weight: bold;
    border-radius: 4px;
}

QPushButton#loadVideoButton:hover {
    background-color: #017785;
}

QPushButton#loadVideoButton:pressed {
    background-color: #029AAB;
}

QPushButton#processVideoButton:disabled {
    background-color: #cecfd0;
    width: 70px;
    height: 50px;
    color: #FFF;
    font-weight: bold;
    border-radius: 4px;
}

QPushButton#processVideoButton:enabled {
    background-color: #015A63;
    width: 70px;
    height: 50px;
    color: #FFF;
    font-weight: bold;
    border-radius: 4px;
}

QPushButton#statisticButton:enabled {
    background-color: #015A63;
    color: #FFF;
    font-weight: bold;
    border-radius: 19px;
}

QPushButton#playButton:enabled {
    background-color: #43b543;
    color: #FFF;
    font-weight: bold;
    border-radius: 19px;
}

QPushButton#trashButton:enabled {
    background-color: #ff4a4a;
    color: #FFF;
    font-weight: bold;
    border-radius: 19px;
}

QPushButton#trashButton:disabled {
    background-color: #a9a9a9a9;
    color: #FFF;
    font-weight: bold;
    border-radius: 19px;
}

QPushButton#statisticButton:disabled {
    background-color: #a9a9a9a9;
    color: #FFF;
    font-weight: bold;
    border-radius: 19px;
}

QPushButton#playButton:disabled {
    background-color: #a9a9a9a9;
    color: #FFF;
    font-weight: bold;
    border-radius: 19px;
}

QPushButton#statisticButton:hover {
    background-color: #017785;
}

QPushButton#statisticButton:pressed {
    background-color: #029AAB;
}

QScrollArea#videosContainer {
    border-radius: 4px;
    border: 1px solid #c9c9c9c9;
    width: 1050px;
    height: 600px;
}

QFrame#videoContainer {
    border: 1px solid #c9c9c9c9;
}

QLabel#videoLabel {
    color: #1F5D63;
    font-weight: bold;
    font-size: 16px;
}

"""
