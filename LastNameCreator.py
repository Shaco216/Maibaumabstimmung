from Crawler import *
from HTML_SearchEngine import *

class LastNameCreator:
    name_cache = []
    _crawler = Crawler()
    _searcher = HTML_SearchEngine()
    def __init__(self):
        self._crawler = Crawler("https://de.wiktionary.org/wiki/Verzeichnis:Deutsch/Namen/die_h%C3%A4ufigsten_Nachnamen_Deutschlands")

    def get_all_Last_Names(self):
        self._searcher = HTML_SearchEngine(MultipleValues=True)
        HTMLpage = self._crawler.Generate_HTML_Code_without_searchword()
        self._searcher.set_HTML_Code(HTMLpage)
        self._searcher.choose_Tag(3)
        self._searcher.search_for("result-name")
        self._searcher.filter_to_only_text()
