import datetime
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.picker import MDThemePicker
from kivymd.toast import toast

from kivy.core.window import Window
Window.size = (400, 750)
# Window.fullscreen = "auto"

import database # import all the database function from database.py as class
connection = database.connect()


class MainPage(ScreenManager): 
    date = StringProperty()
    time = StringProperty()
    sys = NumericProperty()
    dia = NumericProperty()
    pulse = NumericProperty()
    weight = NumericProperty()
    sugar = NumericProperty()

    now = datetime.datetime.now()
    now = now.strftime("Heute %d.%m.%Y - jetzt %H:%M Uhr")
    date_time = StringProperty(now)
    
    def goto_login(self):
        self.current = "Login"

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    
    def check_input(self):
        sys_input = self.ids.sys.text
        dia_input = self.ids.dia.text
        pulse_input = self.ids.pulse.text
        weight_input = self.ids.weight.text
        sugar_input = self.ids.sugar.text
        # print(sys_input, dia_input, pulse_input , weight_input, sugar_input)
        now = datetime.datetime.now()
        date_in = now.strftime("%d.%m.%Y")
        time_in = now.strftime("%H:%M")

        if (len(sys_input) > 1 and  len(sys_input) <= 3) and (len(dia_input) > 1 and 
        len(dia_input) <= 3) and (len(pulse_input) > 1 and len(pulse_input) <= 3) and (len(weight_input) > 1
         and len(weight_input) <= 3) and (len(sugar_input) > 1 and  len(sugar_input) <= 3):
            
            database.store_data(connection,date_in, time_in, sys_input, dia_input,
             pulse_input, weight_input,sugar_input) # call database function from imported class
            
            toast("Eingabe wurde gespeichert !")
            self.ids.sys.text = ""
            self.ids.dia.text = ""
            self.ids.pulse.text = ""
            self.ids.sugar.text = ""
        else:
            toast("Eingabe bitte korrigieren !")

    def export_csv(self):
        database.db_export_csv() # call database function from imported class

            
        
    
class BlutdruckmessenApp(MDApp): 
    date_time = StringProperty
    start_page = StringProperty(None)

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
         

    def build(self):
        return MainPage() # read in the kv-file and build the screen

    

if __name__ == '__main__':
    app = BlutdruckmessenApp()
    app.run()