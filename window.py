import os, sys

from time import sleep

from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class Window():
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])

        # ALL WINDOWS
        self.first_window = uic.loadUi("ui_window\window_one.ui")
        self.timas_window = uic.loadUi("ui_window\window_timas.ui")
        self.java_window = uic.loadUi("ui_window\window_java.ui")
        self.hospital_hall_window = uic.loadUi('ui_window\window_hospital_hall.ui')
        self.morgue_window = uic.loadUi('ui_window\window_morgue.ui')
        self.clown_window = uic.loadUi('ui_window\window_clown.ui')

        self.first_window.show()

        # FIRTS WINDOW BUTTONS
        self.first_window.flepzsButton.clicked.connect(self.flepzs_audio)
        self.first_window.torresButton.clicked.connect(self.torres_audio)
        self.first_window.civicButton.clicked.connect(self.civic_audio)
        self.first_window.fabioButton.clicked.connect(self.fabio_audio)
        self.first_window.timasButton.clicked.connect(self.timas_window_func)
        self.first_window.celsoButton.clicked.connect(self.celso_audio)
        self.first_window.salaButton.clicked.connect(self.sala_audio)
        self.first_window.correctButton.clicked.connect(self.second_window)

        self.player = QMediaPlayer()

        # TIMAS WINDOW BUTTONS
        self.timas_window.pythonButton.clicked.connect(self.timas_audio)
        self.timas_window.javaButton.clicked.connect(self.java_lost)
        self.timas_window.back_first_wButton.clicked.connect(self.back_firts_window)

        # JAVA WINDOW BUTTON
        self.java_window.pushButton.clicked.connect(self.java_to_firts_window)

        # HOSPITAL HALL BUTTONS
        self.hospital_hall_window.cabinetButton.clicked.connect()
        self.hospital_hall_window.doorButton.clicked.connect()
        self.hospital_hall_window.roofButton.clicked.connect()

        # HOSPITAL MORGUE BUTTONS
        self.morgue_window.doorButton.clicked.connect()
        self.morgue_window.clothesButton.clicked.connect()

        # CLOWN BUTTONS
        self.clown_window.noseButton.clicked.connect()
        self.clown_window.footButton.clicked.connect()

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
        self.play_audio('python_na_minha_aula')

    
    def celso_audio(self):
        self.play_audio('errado')
    

    def sala_audio(self):
        ...


    def timas_window_func(self):
        self.first_window.close()
        self.timas_window.show()


    def back_firts_window(self):
        self.timas_window.close()
        self.first_window.show()
        

    def java_lost(self):
        self.play_audio('bixo_vino_mlk')
        sleep(2)
        self.java_window_func()
        
    
    def java_window_func(self):
        self.timas_window.close()
        self.java_window.show()   


    def java_to_firts_window(self):
        self.java_window.close()
        self.first_window.show()
    

    def second_window(self):
        print('DEU CERTO!!')


if __name__ == '__main__':
    window = Window()