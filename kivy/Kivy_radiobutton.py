from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker

kv = """
<Pickers@Screen>
    name: "pickers"

    BoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_y: None
        height: self.minimum_height

        MDRaisedButton:
            text: "Open date picker"
            pos_hint: {"center_x": .5}
            opposite_colors: True
            on_release: app.show_example_date_picker()
        MDLabel:
            id: date_picker_label
            theme_text_color: "Primary"
            halign: "center"

        BoxLayout:
            size_hint: None, None
            size: self.minimum_size
            pos_hint: {"center_x": .5}

            Label:
                theme_text_color: "Primary"
                text: "Start on previous date"
                size_hint_x: None
                width: self.texture_size[0]
                color: 0, 0, 0, 1

            MDCheckbox:
                id: date_picker_use_previous_date
                size_hint: None, None
                size: dp(48), dp(48)
"""
class MainApp(MDApp):
    previous_date = ObjectProperty()

    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Date Picker"
        super().__init__(**kwargs)

    def build(self):
        Builder.load_string(kv)
        self.root = Factory.Pickers()
    
    def show_date_picker(self):
        min_date = datetime.strptime("2020:02:15", '%Y:%m:%d').date()
        max_date = datetime.strptime("2020:05:30", '%Y:%m:%d').date()
        date_dialog = MDDatePicker(
        callback=self.get_date,
        min_date=min_date,
        max_date=max_date,
        )
        date_dialog.open()
"""

    def show_example_date_picker(self, *args):
        if self.root.ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(self.set_previous_date,
                             pd.year, pd.month, pd.day).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()
"""

    def set_previous_date(self, date_obj):
        self.previous_date = date_obj
        self.root.ids.date_picker_label.text = str(date_obj)
if __name__ == "__main__":
    MainApp().run()