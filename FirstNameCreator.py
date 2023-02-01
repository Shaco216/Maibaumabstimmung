from Crawler import *
from HTML_SearchEngine import *
import time

class FirstNameCreator:
    name_cache = []
    _crawler = Crawler()
    _searcher = HTML_SearchEngine()
    def __init__(self):
        self._crawler = Crawler("https://babynames.net/names?page=")


    def search_all_possible_names(self):
        itemsAufSeite = True
        Pagenumber = 1
        self._searcher = HTML_SearchEngine(MultipleValues=True)
        while (itemsAufSeite):
            HTMLpage = self._crawler.Generate_HTML_Code_with_searchword(Pagenumber)
            self._searcher.set_HTML_Code(HTMLpage)
            self._searcher.choose_Tag(1)
            self._searcher.search_for("result-name")
            self._searcher.filter_to_only_text()
            #_searcher.show_current_results()
            for item in self._searcher.get_current_results():
                self.name_cache.append(item)
            Pagenumber = Pagenumber + 1
            time.sleep(3)

    def search_for_limited_amount_of_names(self,Amount):
        counter = 0
        Pagenumber = 1
        self._searcher = HTML_SearchEngine(MultipleValues=True)
        while (Amount > counter):
            HTMLpage = self._crawler.Generate_HTML_Code_with_searchword(Pagenumber)
            self._searcher.set_HTML_Code(HTMLpage)
            self._searcher.choose_Tag(1)
            self._searcher.search_for("result-name")
            self._searcher.filter_to_only_text()
            #_searcher.show_current_results()
            for item in self._searcher.get_current_results():
                self.name_cache.append(item)
                counter = counter + 1
            Pagenumber = Pagenumber + 1
            time.sleep(3)