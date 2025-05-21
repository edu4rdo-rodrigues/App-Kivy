from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Definindo cores (RGBA)
Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Fundo cinza claro

class MeuApp(App):
    def build(self):
        # Layout principal (vertical)
        layout_principal = BoxLayout(orientation='vertical', spacing=10, padding=40)
        
        # Título
        self.titulo = Label(
            text="Meu Primeiro App Kivy",
            font_size=24,
            color=(0, 0, 0.5, 1)  # Azul escuro
        )
        
        # Campo de entrada
        self.entrada = TextInput(
            hint_text="Digite seu nome",
            size_hint=(1, 0.2),
            multiline=False,
            foreground_color=(0, 0, 0, 1)  # Preto
        )
        
        # Botão
        botao = Button(
            text="Saudação",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1),  # Azul
            color=(1, 1, 1, 1)  # Texto branco
        )
        botao.bind(on_press=self.cumprimentar)
        
        # Label para resultado
        self.resultado = Label(
            text="",
            font_size=20,
            color=(0, 0.5, 0, 1)  # Verde
        )
        
        # Adicionando widgets ao layout
        layout_principal.add_widget(self.titulo)
        layout_principal.add_widget(self.entrada)
        layout_principal.add_widget(botao)
        layout_principal.add_widget(self.resultado)
        
        return layout_principal
    
    def cumprimentar(self, instance):
        nome = self.entrada.text
        if nome:
            self.resultado.text = f"Olá, {nome}!"
        else:
            self.resultado.text = "Por favor, digite seu nome!"

if __name__ == "__main__":
    MeuApp().run()