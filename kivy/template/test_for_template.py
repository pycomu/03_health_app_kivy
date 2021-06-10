from logging import root
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDThemePicker
from kivy.core.window import Window
from kivymd.toast import toast
Window.size = (400, 750)

import database # import all the database function from database.py as class
connection = database.connect()
# c = connection.cursor()

class TestPage(ScreenManager): # Screen "TestPage"
    
    # maybe read in T&C text from a file into a variable
    terms_text = StringProperty("""AGREEMENT TO TERMS, \n"""\
        """These Terms and Conditions constitute a legally binding agreement """\
        """made between you, whether personally or on behalf of """\
        """an entity (“you”) and [business entity name] (“we,” “us” or “our”), """\
        """concerning your access to and use of the [website name.com] website as well as """\
        """any other media form, media channel, mobile website or mobile application related, linked, or """\
        """otherwise connected thereto (collectively, the “Site”). You agree that by """\
        """accessing the Site, you have read, understood, and agree to be bound by all of these Terms and Conditions Use.\n"""\
        """IF YOU DO NOT AGREE WITH ALL OF THESE TERMS and CONDITIONS, """\
        """THEN YOU ARE EXPRESSLY PROHIBITED FROM USING THE APP/SITE/SERVICE AND YOU MUST DISCONTINUE USE IMMEDIATELY.""") # variable for text
    
    account_input = StringProperty()
    pin_input = StringProperty()
    re_pin_input = StringProperty()
    email_input = StringProperty()

    child_name_input = StringProperty()
    child_last_input = StringProperty()
    child_age_input = StringProperty()
    child_gender_input = StringProperty()
    

# functions for screen terms & condition +++++++++++++++++++   
    def check_terms(self, value): 
        # print(value)
        if value:
            self.current = "account"
        else:
            toast("Checkbox not clicked !")

# functions for screen account +++++++++++++++++++     
    def create_account(self): 
        if self.ids.pin_input.text == self.ids.re_pin_input.text:
            if self.ids.pin_input.text == "":
                toast("PIN not entered, field is empty!")
            else:
                account_input = self.ids.account_input.text
                pin_input = self.ids.pin_input.text
                email_input = self.ids.email_input.text
                database.store_account(connection, account_input, pin_input, email_input)
                
                self.current = "child" # switching to "child"" screen inside screenamanager
                
        else:
            toast("PIN re-entered is not matching !")
            self.ids.pin_input.text = ""
            self.ids.re_pin_input.text = "" 

# functions for screen child +++++++++++++++++++

    def show_date_picker(self):
        date_dialog = MDDatePicker(min_year=2002, max_year=2021) # child age from 2-16, so calculate min/max from actual year
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    
    def on_save(self, instance, value, date_range): # click okay in date picker
        self.ids.child_age_input.text = str(value)
        ''' Events called when the "OK" dialog box button is clicked.
        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;   '''

    def on_cancel(self, instance, value): # click cancel in date picker
        toast("No (new) child's birthday entered")
        '''Events called when the "CANCEL" dialog box button is clicked.'''

     
    def create_child(self):
        child_name_input = self.ids.child_name_input.text
        print(child_name_input)
        child_last_input = self.ids.child_last_input.text
        print(child_last_input)
        child_age_input = self.ids.child_age_input.text
        print(child_age_input)
        child_gender_input = self.ids.child_gender_input.text
        print(child_gender_input)

        database.store_child_info(connection, child_name_input, child_last_input, child_age_input, child_gender_input)
        

# end of screen functions +++++++++++++++++++++++++++++++++

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