from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

from kivy.network.urlrequest import UrlRequest  # specific for wiki API
import certifi                                  # specific for wiki API

class Home4Screen(Screen):              # this class is initiated in main.py file already

    def wiki_search(self):
        query = self.ids["search_wiki"].text
        if self.ids.search_wiki.text != "":
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
        self.ids["search_result"].text = f"{page_title}\n\n{content}"
        