from tkinter import Tk
import tkinter
from tkinter import *
from FirstNameCreator import *
from LastNameCreator import *
from FullNameRandomizer import *

from EmailAdressCreator import *
from CSV_Creator import *
from PasswordGenerator import *
from UserAdministration import *


class GUI_Maibaum:
    firstname_Collection = FirstNameCreator()
    lastname_collection = LastNameCreator()

    #Savepoints
    savepointOfNames = []
    savepointOfPW = []
    savepointOfEmail = []

    Fenster = tkinter.Tk()
    statustext = "Status: Warte auf Vornamen"

    #TODO: https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
    options = ["v.nachname","vorname.nachname","vorname.n"]
    stringvariable = StringVar(Fenster)
    stringvariable.set(options[0])

    def __init__(self):
        self.Fenster.title('Maibaumabstimmung')
        self.Fenster.geometry('450x320')

        #Labels
        statusLabel = Label(master=self.Fenster, text=self.statustext)
        statusLabel.place(x=135,y=5,width=250,height=20)

        # All Textboxes
        textboxAnzahlVornamen = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlVornamen.insert(END, "Anzahl Vornamen")
        textboxAnzahlVornamen.place(x=55, y=25, width=150, height=20)

        textboxAnzahlNamen = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlNamen.insert(END, "Anzahl Namen")
        textboxAnzahlNamen.place(x=55,y=85,width=150,height=20)

        textboxAnzahlZeichenPasswort = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlZeichenPasswort.insert(END,"Anzahl Passwortzeichen")
        textboxAnzahlZeichenPasswort.place(x=55,y=175, width=150, height=20)

        textboxDomain = Text(master=self.Fenster, bg="Yellow")
        textboxDomain.insert(END, "Domain z.b. web.de")
        textboxDomain.place(x=225,y=25,width=150,height=20)

        textboxSeperator = Text(master=self.Fenster, bg="Yellow")
        textboxSeperator.insert(END, "Seperator auser ;")
        textboxSeperator.place(x=225,y=55,width=150,height=20)

        # All Buttons
        buttonNamenSuchen = Button(master=self.Fenster, bg='DeepSkyBlue2', text='Suche Namen', command=lambda: [statusLabel.config(text=self.change_state_to_suche_namen()),
            self.firstname_Collection.search_for_limited_amount_of_names(int(textboxAnzahlVornamen.get("1.0", END))),
            self.lastname_collection.get_all_Last_Names(),
            self.lastname_collection.rephrase_umlauts(), statusLabel.config(text=self.change_state_to_warte_auf_namenserstellung())])  # mit command= kann man eine methode aufrufen
        buttonNamenSuchen.place(x=55, y=55, width=150, height=20)

        buttonNamenErstellen = Button(master=self.Fenster, bg='DeepSkyBlue2', text="Erstelle Namen",
                                      command=lambda: [statusLabel.config(text=self.change_state_to_erstelle_namensliste()),self.create_point_of_names(int(textboxAnzahlNamen.get("1.0", END))),
                                                       statusLabel.config(text=self.change_state_to_warte_auf_emailadressen())])
        buttonNamenErstellen.place(x=55, y=115, width=150, height=20)

        buttonEmailsErstellen = Button(master=self.Fenster, bg="DeepSkyBlue2", text="Erstelle Emails",command=lambda:
                                        [statusLabel.config(text=self.change_state_to_erzeuge_emails()),
                                         self.create_point_of_emails(textboxDomain.get("1.0",END),optionmenuDesign.grab_current(),textboxSeperator.get("1.0",END)),statusLabel.config(text=self.change_state_to_warte_auf_passwort())])
        buttonEmailsErstellen.place(x=225, y=115, width=150, height=20)
        buttonPasswortErstellen = Button(master=self.Fenster,bg='DeepSkyBlue2', text="Erstelle Passwort",command=lambda: [statusLabel.config(text=self.change_state_to_erstelle_passwort())])
        buttonPasswortErstellen.place(x=55,y=205, width=150, height=20)

        # All Optionmenues
        optionmenuDesign = OptionMenu(self.Fenster, self.stringvariable, *self.options)
        optionmenuDesign.place(x=225,y=85,width=150,height=20)

        self.Fenster.mainloop()

    #ButtonLogik
    def create_point_of_names(self,Amount):
        NameRandomizer = FullNameRandomizer(self.firstname_Collection.name_cache, self.lastname_collection.name_cache)
        NameRandomizer.Create_Multiple_random_names(Amount)
        self.savepointOfNames.append(NameRandomizer)
        #print(NameRandomizer.Get_Namelist())

    def create_point_of_pw(self,Amount):
        pwgen = PWGen()

    def create_point_of_emails(self,domainname,optionOfEmailStructure,seperatorkey):
        EmailCreator = EmailAdressCreator(self.savepointOfNames[0].Get_Namelist())
        EmailCreator.set_domain_name(domainname)
        lengthOfNamelist = len(self.savepointOfNames[0].Get_Namelist())
        print(optionOfEmailStructure)
        optionforEmailCreator = int(optionOfEmailStructure)
        seperatorChar = seperatorkey
        for i in range(lengthOfNamelist):
            EmailCreator.create_email_address_name(optionforEmailCreator, self.savepointOfNames[0].Get_Namelist()[i],
                                                   seperatorChar)
            EmailCreator.create_full_email_with_current_domain_from_currentemail()
            EmailCreator.add_Current_EMailAddress_to_EmailAddressList()
        self.savepointOfEmail.append(EmailCreator)

    #Statusänderungen
    def change_state_to_suche_namen(self):
        self.statustext="Status: Suche Namen..."
        return self.statustext
    def change_state_to_warte_auf_namenserstellung(self):
        self.statustext="Status: Warte auf Namenserstellung"
        return self.statustext
    def change_state_to_erstelle_namensliste(self):
        self.statustext="Status: Erstelle Namensliste..."
        return self.statustext
    def change_state_to_warte_auf_passwort(self):
        self.statustext="Status: Warte auf Passworterstellung"
        return self.statustext
    def change_state_to_erstelle_passwort(self):
        self.statustext="Status: Erstelle Passwort..."
    def change_state_to_warte_auf_emailadressen(self):
        self.statustext="Status: Warte auf Emailerstellung"
        return self.statustext
    def change_state_to_erzeuge_emails(self):
        self.statustext="Status: Erzeuge Emails..."
        return self.statustext

Gui = GUI_Maibaum()


