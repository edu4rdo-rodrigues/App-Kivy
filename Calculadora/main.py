from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class CalculadoraApp(App):
    expressao = ""

    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Fundo escuro
        return Builder.load_file("interface.kv")

    def clique_botao(self, texto_botao):
        if texto_botao == "C":
            self.root.ids.display.text = "0"
            self.expressao = ""
        elif texto_botao == "=":
            try:
                resultado = str(eval(self.expressao))
                self.root.ids.display.text = resultado
                self.expressao = resultado
            except:
                self.root.ids.display.text = "Erro"
                self.expressao = ""
        else:
            if self.root.ids.display.text == "0" or self.root.ids.display.text == "Erro":
                self.root.ids.display.text = ""
            self.expressao += texto_botao
            self.root.ids.display.text += texto_botao

if __name__ == "__main__":
    CalculadoraApp().run()
