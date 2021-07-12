import os
import shutil
import datetime
from logging import root
from sys import path
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.filemanager import MDFileManager
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.picker import MDThemePicker
from kivymd.toast import toast

from kivy.core.window import Window
# Window.size = (400, 750)
# Window.fullscreen = "auto"

from android.permissions import Permission, request_permissions, check_permission
from android.storage import primary_external_storage_path

import database # import all the database function from database.py as class
connection = database.connect()


# ++++++++++++++++++++++++ SCREEN MANAGER +++++++++++++++++++++++++

class MainPage(ScreenManager): 
    date = StringProperty()
    time = StringProperty()
    sys = NumericProperty()
    dia = NumericProperty()
    pulse = NumericProperty()
    weight = NumericProperty()
    sugar = NumericProperty()

    now = datetime.datetime.now()
    now = now.strftime("Today %d.%m.%Y - now %H:%M")
    date_time = StringProperty(now)


# ++++++++++++++++++++++++ THEME PICKER +++++++++++++++++++++++++
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

# ++++++++++++++++++++++++ FUNCTIONS 0f SCREEN MEASURE +++++++++++++++++++++++++
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
            
            now = datetime.datetime.now()
            now = now.strftime("Last submission %d.%m.%Y - %H:%M")
            self.ids.date_time.text = now

            toast("Data entries stored !")
            self.ids.sys.text = ""
            self.ids.dia.text = ""
            self.ids.pulse.text = ""
            self.ids.sugar.text = ""
        else:
            toast("Please correct input values !")

# ++++++++++++++++++++++++ FUNCTIONS 0f SCREEN DIAGRAMM +++++++++++++++++++++++++
    def download_csv(self): # +++ Better create csv file directly on /storage/emulated/0 in database.py ?

        def check_permissions(perms):
            for perm in perms:
                if check_permission(perm) != True:
                    return False
            return True
        
        perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
        
        if  check_permissions(perms)!= True:
            request_permissions(perms)    # get android permissions     
            exit()                        # app has to be restarted; permissions will work on 2nd start
            
        try:
            dst = os.path.join( primary_external_storage_path(),'Download/data_blood.csv')
            
            # toast('creating csv file')
            database.db_export_csv() # call database function from imported class    
            src = "./data_blood.csv"
            shutil.copy (src, dst) # copy and overwrite file

            toast('File stored as: %s' %dst)
        
        except:
            toast('Could not write to external storage ... missing permissions ?') 

            
        
# ++++++++++++++++++++++++ MAIN APP +++++++++++++++++++++++++

class BloodPressureApp(MDApp): 
    
    # start_page = StringProperty(None)

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

     
    def build(self):
        return MainPage() # read in the kv-file and build the screen

    

if __name__ == '__main__':
    app = BloodPressureApp()
    app.run()