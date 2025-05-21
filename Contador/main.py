from kivy.app import App
from kivy.lang import Builder

class MeuApp(App):
    def build(self):
        # Carrega o arquivo kv e retorna o widget raiz que estiver definido diretamente nele
        return Builder.load_file("Contador/interface.kv")

if __name__ == '__main__':
    MeuApp().run()
