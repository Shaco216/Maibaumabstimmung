from bs4 import BeautifulSoup
import requests

#url = "https://babynames.net/names?page=" anschließend kommt seitenauswahl beginnend mit 1
#headers = {
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

class Crawler:
    _url = "" #mit _name wird variable private
    _headers = {}

    def __init__(self, url=""):
        self._url = url
        self._headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def set_URL(self, URL):
        self._url = URL

    def get_URL(self):
        return self._url

    def Generate_HTML_Code_with_searchword(self, Searchword):
        #Header für "emulation" von Gerät

        page = requests.get(self._url + str(Searchword), headers = self._headers)#vorherigersuchlink "https://www.songtexte.com/suche/songs?c=songs&q=" sucht alle ergebnisse gebracht

        if page.status_code == 200:
            content = page.content
        else:
            print("Möglicherweise keine oder keine gute Verbindung zur gewünschten Seite.")
        HTML_Code = BeautifulSoup(content, 'html.parser')
        return HTML_Code

    def Generate_HTML_Code_without_searchword(self):
        page = requests.get(self._url, headers = self._headers)#vorherigersuchlink "https://www.songtexte.com/suche/songs?c=songs&q=" sucht alle ergebnisse gebracht

        if page.status_code == 200:
            content = page.content
        else:
            print("Möglicherweise keine oder keine gute Verbindung zur gewünschten Seite.")
        HTML_Code = BeautifulSoup(content, 'html.parser')
        return HTML_Code

