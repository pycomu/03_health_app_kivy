from logging import root
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, NumericProperty
from kivymd.toast import toast

from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDThemePicker

from kivy.core.window import Window
Window.size = (400, 750)

import database # import all the database function from database.py as class
connection = database.connect()


class MainPage(ScreenManager):
    login_input = StringProperty()

# functions for Login screen +++++++++++++++++++  
    def check_login(self):
        print("PIN entered like: ", self.ids.login_input.text)
        pin = str(self.ids.login_input.text[:4])
        print("PIN cut on 4 digits: ",pin)
        pin_db = database.read_pin_account(connection)
        print(pin_db)
        print(type(pin_db))
        if pin_db == None: # no value yet in table account in database ?
            self.ids.login_input.text = "" # reset input field
            toast("Account not existing, please register")
        else:
            if str(pin) == str(pin_db[0]):
                toast("Login successful")
                self.current = "Home"
            else:
                self.ids.login_input.text = "" # reset input field
                toast("PIN incorrect, account existing?")

    def account_exist(self):
        pin_db = database.read_pin_account(connection)
        if pin_db == None:
            self.current = "Account_terms"
        else:
            toast("Account is existing, remember your PIN!")


# functions for screen terms & condition +++++++++++++++++++ 
   
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
    
    def check_terms(self, value): 
        if value:
            self.current = "Account_adult"
        else:
            toast("Checkbox not clicked !")

# functions for screen account +++++++++++++++++++     
    account_input = StringProperty()
    pin_input = StringProperty()
    re_pin_input = StringProperty()
    email_input = StringProperty()
    
    
    def create_account(self): 
        if self.ids.pin_input.text == self.ids.re_pin_input.text:
            if self.ids.pin_input.text == "":
                toast("PIN not entered, field is empty!")
            else:
                account_input = self.ids.account_input.text
                pin_input = self.ids.pin_input.text
                email_input = self.ids.email_input.text
                database.store_account(connection, account_input, pin_input, email_input)
                
                self.current = "Account_child" # switching to "child"" screen inside screenamanager
                
        else:
            toast("PIN re-entered is not matching !")
            self.ids.pin_input.text = ""
            self.ids.re_pin_input.text = "" 

# functions for screen child +++++++++++++++++++
    child_name_input = StringProperty()
    child_last_input = StringProperty()
    child_age_input = StringProperty()
    child_gender_input = StringProperty()

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
        child_last_input = self.ids.child_last_input.text        
        child_age_input = self.ids.child_age_input.text        
        child_gender_input = self.ids.child_gender_input.text        

        database.store_child_info(connection, child_name_input, child_last_input, child_age_input, child_gender_input)
        
        self.current = "Login" # switching back to "Login"" screen inside screenamanager

# functions for Home screen toolbar +++++++++++++++++++

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

# functions for BMI Tracker screen  +++++++++++++++++++

    child_first_bmi = StringProperty()
    child_height_bmi = NumericProperty
    child_weight_bmi = NumericProperty
    child_age_bmi = NumericProperty
    # child_bmi_calc = NumericProperty

    def store_bmi(self):
        pass

        # database.store_bmi_data(connection,child_first_bmi, child_height_bmi, child_weight_bmi, child_age_bmi, child_bmi_calc, timestamp) 



# App class to build screens +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++     
class ChildHealthApp(MDApp): 
    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

    def build(self):
        return MainPage() # read in the kv-file and build the screen
    

if __name__ == '__main__':
    app = ChildHealthApp()
    app.run()