from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
    

from kivy.core.window import Window
Window.size = (400, 750)



class MainPage(ScreenManager):

    def check_pin(self):
        self.current = "Account"
    
class ChildHealthApp(MDApp): 
    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

    def build(self):
        return MainPage() # read in the kv-file and build the screen

    

if __name__ == '__main__':
    app = ChildHealthApp()
    app.run()