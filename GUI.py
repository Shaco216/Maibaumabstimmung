from tkinter import Tk
import tkinter
from tkinter import *
from FirstNameCreator import *
from LastNameCreator import *
from FullNameRandomizer import *

from EmailAdressCreator import *
from CSV_Creator import *
from Passwordgenerator import *
from UserAdministration import *

firstname_Collection = FirstNameCreator()
lastname_collection = LastNameCreator()

Fenster = tkinter.Tk()
Fenster.title('Maibaumabstimmung')
Fenster.geometry('450x320')

textboxAnzahl = Text(master=Fenster)
textboxAnzahl.insert(END,"Hier Anzahl eingeben")
textboxAnzahl.pack()
buttonVornamenSuchen = Button(master=Fenster, bg='DeepSkyBlue2', text='Suche Vornamen', command=firstname_Collection.search_for_limited_amount_of_names(int(textboxAnzahl.get("1.0",END))))#mit command= kann man eine methode aufrufen
buttonVornamenSuchen.place(x=55, y=55, width=120, height=30)

Fenster.mainloop()