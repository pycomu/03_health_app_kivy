# https://www.techwithtim.net/tutorials/kivy-tutorial/multiple-screens/
# https://www.youtube.com/watch?v=xaYn4XdieCs

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

page = """
WindowManager:   # definition of screenmanager
    MainWindow:
    SecondWindow:

<MainWindow>:
    name: "main"

    GridLayout:
        cols:1

        GridLayout:
            cols: 2

            Label:
                text: "Password: (type 123)"

            TextInput:
                id: passw
                multiline: False

        Button:
            text: "Submit"
            on_release:
                app.root.current = "second" if passw.text == "123" else "main"
                root.manager.transition.direction = "left"


<SecondWindow>:
    name: "second"

    Button:
        text: "Go Back"
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"
"""

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager): # class of screenmanager defined here, no ".add_widget"
    pass


class MyMainApp(App):
    def build(self):
        return Builder.load_string(page)


if __name__ == "__main__":
    MyMainApp().run()