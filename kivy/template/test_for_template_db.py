from logging import root
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager

from kivymd.toast import toast

from kivy.core.window import Window
Window.size = (400, 750)

import database # import all the database function from database.py as class
connection = database.connect()
# c = connection.cursor()

class TestPage(ScreenManager): # Screen "TestPage"
    account_input = StringProperty()
    pin_input = StringProperty()
    re_pin_input = StringProperty()
    email_input = StringProperty()

             
    def create_account(self):
        print("Acc wie eingegebn: ", self.ids.account_input.text)
        print("PIN wie eingegebn: ", self.ids.pin_input.text)
        print("email wie eingegebn: ", self.ids.email_input.text)
        
        if self.ids.pin_input.text == self.ids.re_pin_input.text:
            if self.ids.pin_input.text == "":
                toast("PIN not entered, field is empty!")
            else:
                account_input = self.ids.account_input.text
                pin_input = self.ids.pin_input.text
                email_input = self.ids.email_input.text
                database.store_account(connection, account_input, pin_input, email_input)
                print("account created")

        else:
            toast("PIN re-entered is not matching !")
            self.ids.pin_input.text = ""
            self.ids.re_pin_input.text = ""       
    

class testtemplate_dbApp(MDApp): # design in testtemplate.kv the screen

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
    
          

    def build(self):
        return TestPage() # read in the kv-file and build the screen

if __name__ == '__main__':
    app = testtemplate_dbApp()
    app.run()