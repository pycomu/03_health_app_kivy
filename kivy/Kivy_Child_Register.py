from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (304, 480)

KV = """
MDScreen:
    name: "ChildRegisterPage"
    MDFloatLayout:
        MDFloatLayout:
            id: back
            size_hint_y: .6
            pos_hint: {"center_y": 1.2}
            radius: [0,0,0,40]
            canvas:
                Color:
                    rgb: (0,.4,.8, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos
        MDIconButton:
            id: icon
            icon: "account-child-circle"
            pos_hint: {"center_x": .5, "center_y": .8}
            user_font_size: "60sp"
            theme_text_color: "Custom"
            text_color: 0,.4,.8,1
        MDTextField:
            id: Firstname 
            hint_text: "First Name"
            helper_text: "Please Enter Child's First Name"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            size_hint_x:None
            width:200
        MDTextField:
            id: Lastname 
            hint_text: "Last Name"
            helper_text: "Please Enter Child's Family Name"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            size_hint_x:None
            width:200
        MDTextField:
            id: DOB
            hint_text: "Date of Birth"
            helper_text: "Please Enter Child's Date of Birth"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.4}
            size_hint_x:None
            width:200
        MDRaisedButton:
            text: "Submit"
            pos_hint:{'center_x': 0.5, 'center_y': 0.25}
            size_hint_x: .5
            md_bg_color: 0,.4,.8,1
        
"""

class ChildRegisterApp(MDApp):

    def change_screen(self, name):
        screen_manager.current = ChildRegisterPage
    
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(KV))
        
        return screen_manager

       

if __name__ == '__main__':
    app = ChildRegisterApp()
    app.run()