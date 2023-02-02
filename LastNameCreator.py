from Crawler import *
from HTML_SearchEngine import *

class LastNameCreator:
    name_cache = []
    _crawler = Crawler()
    _searcher = HTML_SearchEngine()
    _result = []
    def __init__(self):
        self._crawler = Crawler("https://de.wiktionary.org/wiki/Verzeichnis:Deutsch/Namen/die_h%C3%A4ufigsten_Nachnamen_Deutschlands")

    def get_all_Last_Names(self):
        self._searcher = HTML_SearchEngine(MultipleValues=True)
        HTMLpage = self._crawler.Generate_HTML_Code_without_searchword()
        self._searcher.set_HTML_Code(HTMLpage)
        self._searcher.choose_Tag(3)
        self._searcher.search_for("/wiki/")
        #self._searcher.filter_to_only_text()
        self._searcher.filter_all_hrefs(["Verzeichnis","Spezial","wikidata","Wiktionary","wikimedia","Hilfe:Hinweise"])
        self._searcher.replacing_all_targeted_characters_in_hrefs_with_one_desired_character(["/wiki/"],"")
        self._result = self._searcher.get_current_results()
        self._searcher.show_current_results()




