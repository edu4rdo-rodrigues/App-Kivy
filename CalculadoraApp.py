from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CalculadoraApp(App):
    def build(self):
        # Layout principal
        layout = GridLayout(cols=4, spacing=5, padding=10)
        
        # Display
        self.display = Label(
            text="0",
            font_size=40,
            size_hint=(1, 0.5),
            halign="right",
            valign="middle"
        )
        layout.add_widget(self.display)
        
        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for botao in botoes:
            btn = Button(
                text=botao,
                font_size=30,
                background_color=(0.7, 0.7, 0.7, 1)
            )
            btn.bind(on_press=self.clique_botao)
            layout.add_widget(btn)
        
        # Estado da calculadora
        self.expressao = ""
        
        return layout
    
    def clique_botao(self, instance):
        texto_botao = instance.text
        
        if texto_botao == "C":
            self.display.text = "0"
            self.expressao = ""
        elif texto_botao == "=":
            try:
                resultado = str(eval(self.expressao))
                self.display.text = resultado
                self.expressao = resultado
            except:
                self.display.text = "Erro"
                self.expressao = ""
        else:
            if self.display.text == "0" or self.display.text == "Erro":
                self.display.text = ""
            self.expressao += texto_botao
            self.display.text += texto_botao

if __name__ == "__main__":
    Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Fundo escuro
    CalculadoraApp().run()