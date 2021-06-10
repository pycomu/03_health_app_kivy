from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.size = (600, 325)


page = ("""
<CustomLabel@Label>:
    text_size: self.size
    valign: "middle"
    padding_x: 5

<SingleLineTextInput@TextInput>:
    multiline: False

<GreenButton@Button>:
    background_color: 1, 1, 1, 1
    size_hint_y: None
    height: self.parent.height * 0.120

UserGroup

    male: chk_male
    female: chk_female
    age: txt_age

    GridLayout:
        cols: 2
        padding : 30,30
        spacing: 20, 20
        row_default_height: '30dp'

        Label:
            text: 'Male'
            text_size: self.size
            valign: 'middle'

        CheckBox:
            group: 'check'
            id : chk_male

        Label:
            text: 'Female'
            text_size: self.size
            valign: 'middle'

        CheckBox:
            group: 'check'
            id: chk_female

        CustomLabel:
            text: 'age'
            text_size: self.size
            valign: 'middle'

        SingleLineTextInput:
            id: txt_age


        GreenButton:
            text: 'Ok'
            on_press: root.insert_data()


        GreenButton:
            text: 'Cancel'
            on_press: app.stop()
""")


class UserGroup(Screen):
    male = ObjectProperty(None)
    female = ObjectProperty(None)
    age = ObjectProperty(None)
    
    def insert_data(self):
        if self.male.active:
            print('Male')
        elif self.female.active:
            print('Female')
        else:
            print('No gender selected')
        print(self.age.text)


class FactUserGroup(App):

    def build(self):
        self.root = Builder.load_string(page)
        return self.root


if __name__ == '__main__':
    FactUserGroup().run()