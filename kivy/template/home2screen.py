from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty

import database # import all the database function from database.py as class
connection = database.connect()

class Home2Screen(Screen):              # this class is initiated in main.py file already

    pin_input = ObjectProperty() # variable for text input inside class
    
    def check_pin(self): # check the entered pin vs database for login and go to home screen
        print("PIN wie eingegebn: ", self.pin_input.text)
        pin = str(self.pin_input.text[:4])
        print("PIN auf 4 Stellen gekürzt: ",pin)

        self.pin_input.text = "" # reset input field

        pin_db = database.read_pin_account(connection)
        # print(pin_db)
        # print(type(pin_db))
        if str(pin) == str(pin_db[0]):
            print("now go to home screen ",pin_db[0])
        else:
            print("PIN is not correct",pin_db[0],"\n")
        