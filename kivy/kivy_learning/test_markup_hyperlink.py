from kivymd.app import MDApp
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
from kivy.lang import Builder # required to have screen definition inside py file

# screen definition
page = '''
Screen:
    MDFloatLayout:
        MDLabel:
            id: LinksLabel
            text: " For URL click on: [ref=https://google.com] [color=#0000ff][u]Google.com[/u][/color] [/ref]"
            text_size: self.width, None
            size_hint_y: None
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            halign: "center"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
'''


class markupApp(MDApp): # main class to build the Login Screen
    def build(self):
        self.login = Builder.load_string(page) # read in screen definition above
        return self.login
    


if __name__ == '__main__':
    markupApp().run()