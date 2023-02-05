"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Script responsável pela inicialização do programa, faz as
    chamadas básicas para iniciar a interface Qt utilizando a
    biblioteca PySide2.
"""

import sys
from PySide2.QtWidgets import QApplication

from src.styles import app_styles
from src.interface import MainWindow
from src.imgproc import create_folder


def main(args):
    """
    Função responsável por criar uma pasta temporária de trabalho e inicializar
    a interface QT utilizando o PySide2.

    [ARGUMENTOS]
        args: Argumentos passados pela chamada do terminal, caso existam.
    """

    create_folder('tmp')

    root = QApplication(args)

    app = MainWindow()
    app.show()

    root.setStyleSheet(app_styles)
    sys.exit(root.exec_())


if __name__ == '__main__':
    main(sys.argv)
