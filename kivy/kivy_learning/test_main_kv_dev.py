from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

from test_kv_def import nav_helper # import now a py-file where the kv code is defined under variable "nav_helper"

Window.size = (300, 500)


class DemoApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        screen = Builder.load_string(nav_helper) # read kv definition
        return screen

    def on_start(self):
        pass


DemoApp().run()