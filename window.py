import os, sys

from time import sleep

from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

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
        self.clebinho_window = uic.loadUi('ui_window\window_clebinho.ui')
        self.wilson_one_window = uic.loadUi('ui_window\window_wilson_one.ui')
        self.wilson_two_window = uic.loadUi('ui_window\window_wilson_two.ui')

        self.first_window.show()

        # FIRTS WINDOW BUTTONS
        self.first_window.flepzsButton.clicked.connect(self.flepzs_audio)
        self.first_window.torresButton.clicked.connect(self.torres_audio)
        self.first_window.civicButton.clicked.connect(self.civic_audio)
        self.first_window.fabioButton.clicked.connect(self.fabio_audio)
        self.first_window.timasButton.clicked.connect(self.timas_window_func)
        self.first_window.celsoButton.clicked.connect(self.celso_audio)
        self.first_window.salaButton.clicked.connect(self.ds7_photo)
        self.first_window.correctButton.clicked.connect(self.second_window)

        self.player = QMediaPlayer()

        #WILSON ONE BUTTONS
        self.wilson_one_window.franButton.clicked.connect(self.fran)
        self.wilson_one_window.lucaButton.clicked.connect(self.luca)
        self.wilson_one_window.wilsonButton.clicked.connect(self.wilson_second)
        self.wilson_one_window.vanessaButton.clicked.connect(self.vanessa)
        self.wilson_one_window.leoButton.clicked.connect(self.leo)
        self.wilson_one_window.backButton.clicked.connect(self.back_main_window2)


        # WILSON TWO BUTTON
        self.wilson_two_window.wilsonButton.clicked.connect(self.clebinho)
        self.wilson_two_window.backButton.clicked.connect(self.back_wilson_one)

        # TIMAS WINDOW BUTTONS
        self.timas_window.pythonButton.clicked.connect(self.timas_audio)
        self.timas_window.javaButton.clicked.connect(self.java_lost)
        self.timas_window.back_first_wButton.clicked.connect(self.back_firts_window)

        # JAVA WINDOW BUTTON
        self.java_window.pushButton.clicked.connect(self.java_to_firts_window)

        # HOSPITAL HALL BUTTONS
        self.hospital_hall_window.cabinetButton.clicked.connect(self.cabinet_audio)
        self.hospital_hall_window.doorButton.clicked.connect(self.opening_the_door)
        self.hospital_hall_window.roofButton.clicked.connect(self.roof_audio)
        self.hospital_hall_window.backButton.clicked.connect(self.back_main_window)

        # HOSPITAL MORGUE BUTTONS
        self.morgue_window.doorButton.clicked.connect(self.nobody_audio)
        self.morgue_window.clothesButton.clicked.connect(self.correct_object)
        self.morgue_window.backButton.clicked.connect(self.back_to_hospital)

        # CLOWN BUTTONS
        self.clown_window.noseButton.clicked.connect(self.horn_audio)
        self.clown_window.footButton.clicked.connect(self.serious_audio)
        self.clown_window.backButton.clicked.connect(self.back_to_murge)

        # CLEBINHO BUTTONS
        self.clebinho_window.backButton.clicked.connect(self.back_main_window3)

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
    

    def ds7_photo(self):
        self.play_audio('certo')
        sleep(2)
        self.first_window.close()
        self.hospital_hall_window.show()


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
        self.play_audio('ooooo')
        sleep(3)
        self.first_window.close()
        # self.clebinho_window.show()
        self.wilson_one_window.show()


    def wilson_second(self):
        self.wilson_one_window.close()
        self.wilson_two_window.show()


    def clebinho(self):
        self.play_audio('Obrigado Deus')
        sleep(5)
        self.wilson_two_window.close()
        self.clebinho_window.show()

    
    def roof_audio(self):
        self.play_audio('ferro')


    def cabinet_audio(self):
        self.play_audio('gustavo_lima')


    def opening_the_door(self):
        self.play_audio('porta_abrindo')
        sleep(5)
        self.hospital_hall_window.close()
        self.morgue_window.show()


    def nobody_audio(self):
        self.play_audio('ninguem')


    def correct_object(self):
        self.play_audio('acertou_mizeravi')
        sleep(3)
        self.morgue_window.close()
        self.clown_window.show()


    def serious_audio(self):
        self.play_audio('ta_tao_serio')
        sleep(5)
        self.clown_window.close()
        self.java_window.show()


    def horn_audio(self):
        self.play_audio('buzina_palhaço')


    def back_main_window(self):
        self.hospital_hall_window.close()
        self.first_window.show()


    def back_to_hospital(self):
        self.morgue_window.close()
        self.hospital_hall_window.show()

    
    def back_to_murge(self):
        self.clown_window.close()
        self.morgue_window.show()


    def fran(self):
        self.play_audio('doutor_fran')

    
    def luca(self):
        self.play_audio('luca')


    def vanessa(self):
        self.play_audio('fail')


    def leo(self):
        self.play_audio('skipt')

    def back_wilson_one(self):
        self.wilson_two_window.close()
        self.wilson_one_window.show()

    def back_main_window2(self):
        self.wilson_one_window.close()
        self.first_window.show()

    def back_main_window3(self):
        self.clebinho_window.close()
        self.wilson_one_window.show()


if __name__ == '__main__':
    window = Window()