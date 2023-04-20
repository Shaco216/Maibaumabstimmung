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


class GUI_Maibaum:
    firstname_Collection = FirstNameCreator()
    lastname_collection = LastNameCreator()
    savepointOfNames = []
    Fenster = tkinter.Tk()
    statustext = "Status: Warte auf Vornamen"

    #TODO: https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
    options = ["v.nachname"]


    def __init__(self):
        self.Fenster.title('Maibaumabstimmung')
        self.Fenster.geometry('450x320')
        #Labels
        statusLabel = Label(master=self.Fenster, text=self.statustext)
        statusLabel.place(x=135,y=5,width=150,height=20)

        # All Textboxes
        textboxAnzahlVornamen = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlVornamen.insert(END, "Anzahl Vornamen")
        textboxAnzahlVornamen.place(x=55, y=25, width=150, height=20)

        textboxAnzahlNamen = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlNamen.insert(END, "Anzahl Namen")
        textboxAnzahlNamen.place(x=55,y=85,width=150,height=20)

        textboxDomain = Text(master=self.Fenster, bg="Yellow")
        textboxDomain.insert(END, "Domain z.b. web.de")
        textboxDomain.place(x=225,y=25,width=150,height=20)

        textboxSeperator = Text(master=self.Fenster, bg="Yellow")
        textboxSeperator.insert(END, "Seperator auser ;")
        textboxSeperator.place(x=225,y=55,width=150,height=20)

        # All Buttons
        buttonNamenSuchen = Button(master=self.Fenster, bg='DeepSkyBlue2', text='Suche Namen', command=lambda: [
            self.firstname_Collection.search_for_limited_amount_of_names(int(textboxAnzahlVornamen.get("1.0", END))),
            self.lastname_collection.get_all_Last_Names(),
            self.lastname_collection.rephrase_umlauts(), statusLabel.config(text=self.change_state_to_warte_auf_namenserstellung())])  # mit command= kann man eine methode aufrufen
        buttonNamenSuchen.place(x=55, y=55, width=150, height=20)

        buttonNamenErstellen = Button(master=self.Fenster, bg='DeepSkyBlue2', text="Erstelle Namen",
                                      command=lambda: self.create_point_of_names(int(textboxAnzahlNamen.get("1.0", END))))
        buttonNamenErstellen.place(x=55, y=115, width=150, height=20)

        self.Fenster.mainloop()

    def create_point_of_names(self,Amount):
        NameRandomizer = FullNameRandomizer(self.firstname_Collection.name_cache, self.lastname_collection.name_cache)
        NameRandomizer.Create_Multiple_random_names(Amount)
        self.savepointOfNames.append(NameRandomizer)
        print(NameRandomizer.Get_Namelist())
    def change_state_to_warte_auf_namenserstellung(self):
        self.statustext="Status: Warte auf Namenserstellung"
        return self.statustext



Gui = GUI_Maibaum()


