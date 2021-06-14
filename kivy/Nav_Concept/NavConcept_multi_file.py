from kivymd.app import MDApp
# from kivy.lang import Builder # no need at multi files
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.picker import MDThemePicker

from kivymd.uix.list import OneLineIconListItem, MDList

from kivy.core.window import Window
Window.size = (400, 750)



class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty() # because in seperate kv file
    nav_drawer = ObjectProperty()
    
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

class Screen3(Screen):
    screen_manager = ObjectProperty() # because in seperate kv file
    nav_drawer = ObjectProperty()

class Def_Screen(BoxLayout): # name of screen in navconcept_multi_file.kv
    pass

class NavConcept_multi_file(MDApp):
    
    def build(self):
        return Def_Screen()

if __name__ == '__main__':
    app = NavConcept_multi_file()
    app.run()
