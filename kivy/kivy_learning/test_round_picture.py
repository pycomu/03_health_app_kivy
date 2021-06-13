from kivymd.app import MDApp

from kivy.lang import Builder # required to have screen definition inside py file
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.toast import toast

Window.size = (400, 750)

# screen definition
page = '''
Screen:
    MDCard:
        id : card
        size_hint: .85, .85
        pos_hint: {"center_x": .5, "center_y": .5}
        orientation: "vertical"
        elevation: 12
        
        BoxLayout:
            FloatLayout:
                canvas:
                    Color:
                        rgb: 1, 1, 1
                    Ellipse:
                        pos: 100, 50
                        size: 150 , 150 
                        source: "img/ai_portraet.jpg"
                        angle_start: 0
                        angle_end: 360
            FloatLayout:    
                canvas:
                    Color:
                        rgb: 1, 1, 1
                    Ellipse:
                        pos: 100, 250
                        size: 150 , 150  
                        source: "img/happy_monster.jpeg"
                        angle_start: 0
                        angle_end: 360
            FloatLayout:    
                canvas:
                    Color:
                        rgb: 1, 1, 1
                    Ellipse:
                        pos: 100, 450
                        size: 150 , 150  
                        source: "img/pycomu.png"
                        angle_start: 0
                        angle_end: 360
            FloatLayout:    
                canvas:
                    Color:
                        rgb: 1, 1, 1
                    Ellipse:
                        pos: 100, 650
                        size: 150 , 150  
                        source: "img/robot.png"
                        angle_start: 0
                        angle_end: 360
        
'''


class mdcardApp(MDApp): # main class to build the Login Screen
    def build(self):
        self.login = Builder.load_string(page) # read in screen definition above
        return self.login
    


if __name__ == '__main__':
    mdcardApp().run()