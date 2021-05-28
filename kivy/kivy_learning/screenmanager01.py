# https://github.com/attreyabhatt/KivyMD-Basics/blob/master/13%20-%20Switching%20Screens/main.py
# https://www.youtube.com/watch?v=u3Ue6IlzbOE

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

page = """
ScreenManager:   # definition of screenmanager
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'
    
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


# Create the class screen manager in python part with 3 screens
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):

    def build(self):
        return Builder.load_string(page)


DemoApp().run()