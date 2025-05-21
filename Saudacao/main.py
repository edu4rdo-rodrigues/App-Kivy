from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 0.9, 1)

class MeuApp(App):
    def build(self):
        return Builder.load_file("Saudacao/interface.kv")  # Caminho correto para seu projeto

    def cumprimentar(self):
        nome = self.root.ids.entrada.text
        if nome:
            self.root.ids.resultado.text = f"Olá, {nome}!"
        else:
            self.root.ids.resultado.text = "Por favor, digite seu nome!"

if __name__ == "__main__":
    MeuApp().run()
