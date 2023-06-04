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
        self.timas_window = uic.loadUi("ui_window\window_timas.ui")
        self.first_window.show()

        self.first_window.flepzsButton.clicked.connect(self.flepzs_audio)
        self.first_window.torresButton.clicked.connect(self.torres_audio)
        self.first_window.civicButton.clicked.connect(self.civic_audio)
        self.first_window.fabioButton.clicked.connect(self.fabio_audio)
        self.first_window.timasButton.clicked.connect(self.timas_window_func)
        self.first_window.celsoButton.clicked.connect(self.celso_audio)
        self.first_window.salaButton.clicked.connect(self.sala_audio)
        self.first_window.correctButton.clicked.connect(self.second_window)

        self.player = QMediaPlayer()

        app.exec()

    
    def play_audio(self, audio_name):
        full_audio_path = os.path.join(os.getcwd(), f'audios\{audio_name}.mp3')
        url = QUrl.fromLocalFile(full_audio_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()

    
    def flepzs_audio(self):
        self.play_audio('mim_de_papai')


    def torres_audio(self):
        self.play_audio('indiano')

    
    def civic_audio(self):
        self.play_audio('civic_si')
    

    def fabio_audio(self):
        self.play_audio('a_mimir')

    
    def timas_audio(self):
        self.play_audio('')

    
    def celso_audio(self):
        self.play_audio('errado')
    

    def sala_audio(self):
        ...

    def timas_window_func(self):
        self.first_window.close()
        self.timas_window.show()
    
    

    def second_window(self):
        print('DEU CERTO!!')


if __name__ == '__main__':
    window = Window()