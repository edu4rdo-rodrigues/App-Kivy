#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex

# Registrar fonte personalizada (opcional)
LabelBase.register(name='Roboto',
                  fn_regular='assets/fonts/Roboto-Regular.ttf',
                  fn_bold='assets/fonts/Roboto-Bold.ttf')

class Interface(BoxLayout):
    contador = StringProperty('0')
    
    def incrementar(self):
        self.contador = str(int(self.contador) + 1)
    
    def decrementar(self):
        self.contador = str(int(self.contador) - 1)

class MeuAppKivy(App):
    def build(self):
        self.title = "App Python3/Kivy"
        return Interface()

if __name__ == '__main__':
    MeuAppKivy().run()