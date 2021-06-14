from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty
from kivymd.uix.picker import MDThemePicker

from kivymd.uix.list import OneLineIconListItem, MDList

from kivy.core.window import Window
Window.size = (400, 750)

KV = '''
<ContentNavigationDrawer>:
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
        text: "Children Health App"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "by PyCoMu"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:
        
        MDList:
            id: md_list

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Screen1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Screen2"
            
            OneLineListItem:
                text: "Screen 3"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Screen3"

            OneLineIconListItem:
                text: "Theme"
                on_press:
                    root.show_theme_picker()
                IconLeftWidget:
                    icon: 'theme-light-dark'

Screen:

    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            Screen:
                name: "Screen1"
                id: screen1
                
                BoxLayout:
                    orientation: 'vertical'

                    # try to put as template ond day ?
                    MDToolbar: 
                        title: "Toolbar of Screen 1"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    BoxLayout: # Boxlayout for all other widgets on screen 1
                        orientation: 'vertical'
                        MDLabel:
                            text: "Screen 1 with toolbar"
                            halign: "center" 
                        MDRaisedButton:
                            text: "back to Screen 2 without toolbar"
                            pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                            on_release:
                                screen_manager.current = "Screen2"
            Screen:
                name: "Screen2"
                id: screen2
                
                BoxLayout:
                    orientation: 'vertical'

                    BoxLayout: # Boxlayout for all other widgets on screen 1
                        orientation: 'vertical'
                        MDLabel:
                            text: "Screen 2 without toolbar"
                            halign: "center"
                        MDRaisedButton:
                            text: "back to Screen 1 with toolbar"
                            pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                            on_release:
                                screen_manager.current = "Screen1"

            Screen:
                name: "Screen3"
                id: screen3
                
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar: 
                        title: "Toolbar of Screen 3"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    BoxLayout: # Boxlayout for all other widgets on screen 3
                        orientation: 'vertical'
                        MDLabel:
                            text: "Screen 3 with toolbar"
                            halign: "center" 
                        MDRaisedButton:
                            text: "back to Screen 2 without toolbar"
                            pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                            on_release:
                                screen_manager.current = "Screen2"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

      
'''

class ContentNavigationDrawer(BoxLayout):
    pass
    # screen_manager = ObjectProperty() # later when in a seperate kv file
    # nav_drawer = ObjectProperty()
    
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()



class NavConcept_one_file(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    app = NavConcept_one_file()
    app.run()