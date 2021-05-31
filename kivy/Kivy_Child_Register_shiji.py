from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.uix.picker import MDDatePicker

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
        MDToolbar:
            title: "Register Child"
            pos_hint: {"top": 1}
            elevation: 10
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
            text: "Open Date picker"
            pos_hint: {'center_x': 0.7, 'center_y': 0.4}
            on_release: app.show_date_picker()
        MDRaisedButton:
            text: "Submit"
            pos_hint:{'center_x': 0.5, 'center_y': 0.1}
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
  
    
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    """
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    """
    def show_date_picker(self):
        date_dialog = MDDatePicker(min_year=1990, max_year=2032)
        date_dialog.open()


if __name__ == '__main__':
    app = ChildRegisterApp()
    app.run()
