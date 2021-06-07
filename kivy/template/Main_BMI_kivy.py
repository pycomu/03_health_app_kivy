from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDThemePicker
from kivy.properties import ObjectProperty
# from kivy.clock import Clock
# Clock.max_iteration = 20

from home4screen import Home4Screen # import the functions used in this screen 
from home2screen import Home2Screen

from kivy.core.window import Window
Window.size = (400, 750)



class Home4Screen(Screen):
    pass

class Home3Screen(Screen):
    pass

class Home2Screen(Screen):
    pass

class HomeScreen(Screen):
    pass

 
        
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

class ChildHealthApp(MDApp):

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        
    

    def build(self):
        return

if __name__ == '__main__':
    app = ChildHealthApp()
    app.run()