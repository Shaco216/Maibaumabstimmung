from Crawler import *

crawler = Crawler("https://babynames.net/names?page=")
itemsAufSeite = True
Seitenzahl = 1
while (itemsAufSeite):
    HTMLpage = crawler.HTML_Code_Generieren(Seitenzahl)

    Seitenzahl = Seitenzahl+1