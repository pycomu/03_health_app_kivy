from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "MDToolbar"
            left_action_items: [["menu", lambda x: nav_draw.set_state()]]
        Widget:
    MDNavigationLayout:    # see at https://kivymd.readthedocs.io/en/0.104.0/components/navigation-drawer/index.html
        ScreenManager:
            id: screen_manager
            Screen:
                name: "scr1"
                MDLabel:
                    text: "Screen 1"
                    halign: "center"
        
            Screen:
                name: "scr2"
                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                        
        MDNavigationDrawer:
            id: nav_draw
            orientation: "vertical"
            padding: "8dp"
            spacing: "8dp"
            
            AnchorLayout:
                anchor_x: "left"
                size_hint_y: None
                height: avatar.height
    
                Image:
                    id: avatar
                    size_hint: None, None
                    size: "56dp", "56dp"
                    source: "data/logo/kivy-icon-256.png"
    
            MDLabel:
                text: "Kaustubh Gupta"
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]
        
            MDLabel:
                text: "youreamil@gmail.com"
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]
            
            ScrollView:
                MDList:
                    OneLineAvatarListItem:
                        on_press:
                            #nav_draw.set_state("close")
                            screen_manager.current = "scr1"
    
                        text: "Home"
                        IconLeftWidget:
                            icon: "home"
    
                    OneLineAvatarListItem:
                        on_press:
                            nav_draw.set_state("close")
                            screen_manager.current = "scr2"
                        text: "About"
                        IconLeftWidget:
                            icon: 'information'
                                
            Widget:
"""

class Main(MDApp):

    def build(self):
        return Builder.load_string(kv)


Main().run()