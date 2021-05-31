from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)


MDFloatLayout:
    BoxLayout:
        orientation: "horizontal"
        MDLabel:
            halign:"center"
            text:"Male"
            pos_hint: {'center_x': .2}
        Check:
            active: True
            pos_hint: {'center_x': .4, 'center_y': .5}

        MDLabel:
            halign:"center"
            text:"Female"
            pos_hint: {'center_x': .6}
            
        Check:
            active: True
            pos_hint: {'center_x': .8, 'center_y': .5}
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()