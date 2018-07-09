import threading
import time

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from load import *


class Meni(Screen):
    zvuk = SoundLoader.load("zvukovi/click.mp3")
    background = SoundLoader.load("zvukovi/pozadinska.mp3")
    background.loop = True
    background.volume = 0.5
    background.play()


    def click_sound(self):
        self.zvuk.play()



class StartScreen(Screen):
    zvuk = SoundLoader.load("zvukovi/click.mp3")

    def click_sound(self):
        self.zvuk.play()



class GameActionScreen(Screen):
    greske = 0
    runda = 1
    max_rundi = 5

    task_values = [0, 0, 0, 0, 0]

    vrsta = 2

    def new_game(self):
        self.Tasks = Loader()
        self.runda = 0
        t1 = threading.Thread(target=self.load_sounds)
        t1.start()
        self.set_next_task()

    def set_next_task(self):
        self.task_values = self.Tasks.load(self.vrsta)
        self.ids.task.text = self.task_values[0]
        self.ids.button_1.text = str(self.task_values[2])
        self.ids.button_2.text = str(self.task_values[3])
        self.ids.button_3.text = str(self.task_values[4])
        self.ids.button_4.text = str(self.task_values[5])

        self.ids.label_1.text = "Greske: " + str(self.greske)
        self.ids.label_2.text = str(self.runda) + " / " + str(self.max_rundi)

        self.ids.button_1.background_normal = "./slike/normal.png"
        self.ids.button_2.background_normal = "./slike/normal.png"
        self.ids.button_3.background_normal = "./slike/normal.png"
        self.ids.button_4.background_normal = "./slike/normal.png"

    def check_answer(self, button_pressed):
        if button_pressed.text == self.task_values[1]:
            t1 = threading.Thread(target=self.correct_sound)
            t1.start()

            button_pressed.background_normal = './slike/tacno.png'

            self.runda += 1
            self.ids.label_2.text = str(self.runda) + " / " + str(self.max_rundi)
        else:
            t1 = threading.Thread(target=self.wrong_sound)
            t1.start()

            self.runda += 1
            self.ids.label_2.text = str(self.runda) + " / " + str(self.max_rundi)
            self.greske += 1
            self.ids.label_1.text = "Greske: " + str(self.greske)

            self.ids.task.markup = True

            button_pressed.background_normal = './slike/greska.png'

        if self.runda == self.max_rundi:
            self.manager.current = 'result'
        else:
            t2 = threading.Thread(target=self.response)
            t2.start()

    def load_sounds(self):
        self.sounds = {}
        self.sounds[0] = SoundLoader.load("zvukovi/correct.ogg")
        self.sounds[1] = SoundLoader.load("zvukovi/wrong.ogg")

    def correct_sound(self):
        self.sounds[0].play()

    def wrong_sound(self):
        self.sounds[1].play()

    def response(self):
        time.sleep(1)
        self.ids.button_1.disabled = True
        self.ids.button_2.disabled = True
        self.ids.button_3.disabled = True
        self.ids.button_4.disabled = True
        time.sleep(1)
        self.ids.button_1.disabled = False
        self.ids.button_2.disabled = False
        self.ids.button_3.disabled = False
        self.ids.button_4.disabled = False

        self.set_next_task()


class ResultScreen(Screen):
    zvuk = SoundLoader.load("zvukovi/click.mp3")

    def click_sound(self):
        self.zvuk.play()

    def calculate_result(self, screen):
        if screen.greske <= 1:
            self.ids.star_5.source = './slike/zvezda.png'
            self.ids.star_4.source = './slike/zvezda.png'
            self.ids.star_3.source = './slike/zvezda.png'
            self.ids.star_2.source = './slike/zvezda.png'
            self.ids.star_1.source = './slike/zvezda.png'
            self.ids.label.text = 'Svaka cast!\n\n'
        elif screen.greske <= 2:
            self.ids.star_4.source = './slike/zvezda.png'
            self.ids.star_3.source = './slike/zvezda.png'
            self.ids.star_2.source = './slike/zvezda.png'
            self.ids.star_1.source = './slike/zvezda.png'
            self.ids.label.text = 'Vrlo dobro!\n\n Ali moze bolje!'
        elif screen.greske <= 3:
            self.ids.star_3.source = './slike/zvezda.png'
            self.ids.star_2.source = './slike/zvezda.png'
            self.ids.star_1.source = './slike/zvezda.png'
            self.ids.label.text = 'Solidan!\n\n'
        elif screen.greske <= 4:
            self.ids.star_2.source = './slike/zvezda.png'
            self.ids.star_1.source = './slike/zvezda.png'
            self.ids.label.text = 'Lose\n\n Probaj ponovo kad naucis nesto!'
        else:
            self.ids.label.text = 'Magare!\n\n Pojma nemas!'

class AboutScreen(Screen):
    zvuk = SoundLoader.load("zvukovi/click.mp3")

    def click_sound(self):
        self.zvuk.play()

    def about_text(self):
        return "CS324 - Skripting jezici - projekat\n" \
               "\n" \
               "Projektni zadatak iz predmeta CS324 radjen u Pythonu\n" \
               "Korisceni framework : Kivy\n" \
               "                        Darko Stojanovic"


class PopUpQuit(Popup):
    pass


class KvizApp(App):
    sm = ScreenManager(transition=FadeTransition())

    def build(self):
        self.sm.add_widget(Meni(name='menu'))
        self.sm.add_widget(StartScreen(name='start'))
        self.sm.add_widget(AboutScreen(name='about'))
        self.sm.add_widget(GameActionScreen(name='game'))
        self.sm.add_widget(ResultScreen(name='result'))
        Window.bind(on_keyboard=self.handle_keyboard)

        self.title = 'Kivy kviz'

        return self.sm

    def handle_keyboard(self, window, key, *largs):
        if key == 27 or key == 273:
            if self.sm.current_screen.name == 'game':
                popup = PopUpQuit()
                popup.open()
            elif self.sm.current_screen.name == 'menu':
                quit()

            return True


if __name__ == '__main__':
    KvizApp().run()