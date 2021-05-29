from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.core.window import Window
Window.size = (400, 750)

from kivy.network.urlrequest import UrlRequest
import certifi

class TestPage(MDFloatLayout): # Screen "TestPage"
    pass
    
    
class testtemplateApp(MDApp): # design in testtemplate.kv the screen

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
    
    def wiki_search_button(self):
        query = self.root.ids["search_wiki"].text
        if self.root.ids.search_wiki.text != "":
            self.get_data(title=query)

    def get_data(self, *args, title=None):
        if title == None:
            response = args[1]
            random_article = response["query"]["random"][0]
            title = random_article["title"]
        endpoint = f"https://en.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={title.replace(' ', '%100')}"
        self.data_request = UrlRequest(endpoint,
                                       on_success=self.set_textarea,
                                       ca_file=certifi.where())

    def set_textarea(self, request, response):
        page_info = response["query"]["pages"]
        page_id = next(iter(page_info))
        page_title = page_info[page_id]["title"]
        try:
            content = page_info[page_id]["extract"]
        except KeyError:
            content = f"Sorry, but your search '{page_title}' got no results!\n\nPlease try again! "
        self.root.ids["search_result"].text = f"{page_title}\n\n{content}"
        

    def build(self):
        return TestPage() # read in the kv-file and build the screen

if __name__ == '__main__':
    app = testtemplateApp()
    app.run()