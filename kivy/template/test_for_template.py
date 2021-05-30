from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty

from kivy.core.window import Window
Window.size = (400, 750)

import database # import all the database function from database.py as class
connection = database.connect()
# c = connection.cursor()

class TestPage(MDFloatLayout): # Screen "TestPage"
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
            print("PIN is not correct",pin_db[0])

    
class testtemplateApp(MDApp): # design in testtemplate.kv the screen

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
    
    
        

    def build(self):
        return TestPage() # read in the kv-file and build the screen

if __name__ == '__main__':
    app = testtemplateApp()
    app.run()