import os, sys

from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class Window():
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])

        self.first_window = uic.loadUi("ui_window\window_one.ui")
        self.first_window.show()

        self.first_window.flepzsButton.clicked.connect(self.flepzs_audio)
        self.first_window.torresButton.clicked.connect(self.torres_audio)
        self.first_window.correctButton.clicked.connect(self.classmates_btn)

        self.player = QMediaPlayer()

        app.exec()

    
    def flepzs_audio(self):
        full_audio_path = os.path.join(os.getcwd(), 'audios\mim_de_papai.mp3')
        url = QUrl.fromLocalFile(full_audio_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()


    def torres_audio(self):
        full_audio_path = os.path.join(os.getcwd(), 'audios\indiano.mp3')
        url = QUrl.fromLocalFile(full_audio_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
    
    

    def torres_btn(self):
        print('TORRES GAYZÃO')

    def classmates_btn(self):
        print('DEU CERTO!!')


if __name__ == '__main__':
    window = Window()