# https://www.youtube.com/watch?v=MihVMtret20
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa3ZfTmZUVjl5RjdYTHVMaGZ6bTlRX3BpWmUyd3xBQ3Jtc0tsZmhTMThCZ3owNk1OaDh3b2pjNFZzTEM1OUpzeGV1SENVYzZzcHNXRGJZblhtVkNiaHl5R3R2Y244aTYzaGI1cXZKbEhWNC1IN1ZIWXVUWkxGckNHNGtRMi1yN2dxcXFiODVXaDBwUkxyTEZOa2dlMA&q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F19FcrzXzofgcusJ6A-zUnYkORlTPErEvI%2Fview%3Fusp%3Dsharing

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from kivy.core.window import Window
Window.size = (400, 750)



class TestPage(ScreenManager): # Screen "TestPage"
    pass
    
class test_screenmanager04App(MDApp): # design in testtemplate.kv the screen

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

    def build(self):
        return TestPage() # read in the kv-file and build the screen

if __name__ == '__main__':
    app = test_screenmanager04App()
    app.run()