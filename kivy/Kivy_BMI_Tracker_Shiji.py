from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.uix.picker import MDDatePicker

Window.size = (304, 480)

KV = """
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)

MDScreen:
    name: "ChildBMIPage"
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
            icon: "calculator"
            pos_hint: {"center_x": .5, "center_y": .8}
            user_font_size: "60sp"
            theme_text_color: "Custom"
            text_color: 0,.4,.8,1
        MDToolbar:
            title: "BMI Tracker"
            pos_hint: {"top": 1}
            elevation: 10
        MDTextField:
            id: Childname 
            hint_text: "Child Name"
            helper_text: "Please Enter Child's Name"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            size_hint_x:None
            width:200
        MDIconButton:
            id: icon
            icon: "human-child"
            pos_hint: {"center_x": 0.8, "center_y": 0.6}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: 0,.4,.8,1
        MDTextField:
            id: Height 
            hint_text: "Height"
            helper_text: "Please Enter Child's Height in cm"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            size_hint_x:None
            width:200
        MDIconButton:
            id: icon
            icon: "human-male-height"
            pos_hint: {"center_x": 0.8, "center_y": 0.5}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: 0,.4,.8,1
        MDTextField:
            id: Weight
            hint_text: "Weight"
            helper_text: "Please Enter Child's Weight in Kg"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            size_hint_x:None
            width:200 
        MDIconButton:
            id: icon
            icon: "weight-kilogram"
            pos_hint: {"center_x": 0.8, "center_y": 0.4}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: 0,.4,.8,1
        MDTextField:
            id: BMI
            hint_text: "BMI Calculated"
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            size_hint_x:None
            width:200        
        MDRaisedButton:
            text: "Submit"
            pos_hint:{'center_x': 0.5, 'center_y': 0.1}
            size_hint_x: .5
            md_bg_color: 0,.4,.8,1
       
"""

class ChildBMIApp(MDApp):

    def change_screen(self, name):
        screen_manager.current = ChildBMIPage
    
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(KV))
        
        return screen_manager



if __name__ == '__main__':
    app = ChildBMIApp()
    app.run()
