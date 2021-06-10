from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker

KV = '''
MDFloatLayout:

    MDToolbar:
        title: "MDDatePicker"
        pos_hint: {"top": 1}
        elevation: 10

    MDRaisedButton:
        text: "Open Date picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
'''


class Dateentry(MDApp):
    def build(self):
        return Builder.load_string(KV)

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


Dateentry().run()