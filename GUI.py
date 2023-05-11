from tkinter import Tk
import tkinter
from tkinter import *
from tkinter import filedialog
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

    #region Savepoints
    savepointOfNames = []
    savepointOfPW = []
    savepointOfEmail = []
    savepointOfZusammenfassung = []
    #endregion

    Fenster = tkinter.Tk()
    statustext = "Status: Warte auf Vornamen"
    pathtext = "Pfad: "

    #https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
    options = ["v.nachname","vorname.nachname","vorname.n"]

    #region stringvariablen
    #statustext
    stringvariableStatus = StringVar(Fenster)
    stringvariableStatus.set(options[0])
    #endregion

    def __init__(self):
        self.Fenster.title('Maibaumabstimmung')
        self.Fenster.geometry('450x320')
        self.Fenster.iconbitmap('Pinguinware.ico')

        #region All Labels
        statusLabel = Label(master=self.Fenster, text=self.statustext)
        statusLabel.place(x=85,y=5,width=250,height=20)

        pathLabel = Label(master=self.Fenster, text=self.pathtext)
        #endregion

        #region All Textboxes
        textboxAnzahlVornamen = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlVornamen.insert(END, "Anzahl Vornamen")
        textboxAnzahlVornamen.place(x=55, y=25, width=150, height=20)

        textboxAnzahlNamen = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlNamen.insert(END, "Anzahl Namen")

        textboxAnzahlZeichenPasswort = Text(master=self.Fenster, bg="Yellow")
        textboxAnzahlZeichenPasswort.insert(END,"Anzahl Passwortzeichen")

        textboxDomain = Text(master=self.Fenster, bg="Yellow")
        textboxDomain.insert(END, "Domain z.b. web.de")

        textboxSeperator = Text(master=self.Fenster, bg="Yellow")
        textboxSeperator.insert(END, "Trennzeichen ausser ;")
        #endregion

        #region All Buttons
        #lambda funktion checkt noch nicht, dass ; nicht eingegeben werden darf
        buttonNamenSuchen = Button(master=self.Fenster, bg='DeepSkyBlue2', text='Suche Vornamen', command=lambda : [
            statusLabel.config(text=self.change_state_to_suche_namen()),
            self.firstname_Collection.search_for_limited_amount_of_names(int(textboxAnzahlVornamen.get("1.0", END))),
            self.lastname_collection.get_all_Last_Names(),
            self.lastname_collection.rephrase_umlauts(), statusLabel.config(text=self.change_state_to_warte_auf_namenserstellung()),
            buttonNamenErstellen.place(x=55, y=115, width=150, height=20),textboxAnzahlNamen.place(x=55,y=85,width=150,height=20)]
            if textboxSeperator.get("1.0", END) != ";" else textboxSeperator.config(text="Falsche Eingabe"))   # mit command= kann man eine methode aufrufen
        buttonNamenSuchen.place(x=55, y=55, width=150, height=20)

        buttonNamenErstellen = Button(master=self.Fenster, bg='DeepSkyBlue2', text="Erstelle Namen",
                                      command=lambda: [statusLabel.config(text=self.change_state_to_erstelle_namensliste()),
                                                       self.create_point_of_names(int(textboxAnzahlNamen.get("1.0", END))),
                                                       statusLabel.config(text=self.change_state_to_warte_auf_emailadressen()),
                                                       buttonEmailsErstellen.place(x=225, y=115, width=150, height=20),
                                                       textboxDomain.place(x=225,y=25,width=150,height=20),
                                                       textboxSeperator.place(x=225,y=55,width=150,height=20),
                                                       optionmenuDesign.place(x=225,y=85,width=150,height=20)])

        buttonEmailsErstellen = Button(master=self.Fenster, bg="DeepSkyBlue2", text="Erstelle Emails",command=lambda:
                                        [statusLabel.config(text=self.change_state_to_erzeuge_emails()),
                                         self.create_point_of_emails(textboxDomain.get("1.0",END),
                                                                     self.stringvariableStatus.get(),
                                                                     textboxSeperator.get("1.0",END)),
                                        statusLabel.config(text=self.change_state_to_warte_auf_passwort()),
                                         buttonPasswortErstellen.place(x=55,y=205, width=150, height=20),
                                         textboxAnzahlZeichenPasswort.place(x=55,y=175, width=150, height=20)])

        buttonPasswortErstellen = Button(master=self.Fenster, bg='DeepSkyBlue2', text="Erstelle Passwortgenerator",command=lambda:
                                        [statusLabel.config(text=self.change_state_to_erstelle_passwort()),
                                         self.create_point_of_pw(int(textboxAnzahlZeichenPasswort.get("1.0",END))),
                                         statusLabel.config(text=self.change_state_to_warte_auf_Email_Passwoerter_Zuordnung()),
                                         buttonZuordnungEMailPasswort.place(x=225,y=205,width=150,height=20)])

        buttonZuordnungEMailPasswort = Button(master=self.Fenster, bg='DeepSkyBlue2', text="Ordne Passwörter zu User", command=lambda:
                                              [statusLabel.config(text=self.change_state_to_ordne_Email_zu_Passwoerter_zu()),
                                               self.create_point_of_Userzusammenfassung(),
                                               statusLabel.config(text=self.change_state_to_warte_auf_csv_erstellung()),
                                               buttonErstelleCSV.place(x=55, y=260, width=320, height=20),buttonChooseSaveDir.place(x=225,y=175,width=150,height=20)])


        buttonErstelleCSV = Button(master=self.Fenster, bg='LawnGreen', text="Erstelle CSV",
                                              command=lambda:
                                              [statusLabel.config(
                                                  text=self.change_state_to_erstelle_csv()),
                                               self.create_csv(),
                                              statusLabel.config(text=self.change_state_to_csv_fertig())])

        buttonChooseSaveDir = Button(master=self.Fenster, bg='DeepSkyBlue2', text="Speicherort festlegen", command=lambda: [self.openDir(),pathLabel.place(x=85, y=230, width=250, height=20),
                                    pathLabel.config(text=self.change_path_state())])

        #endregion

        #region All Optionmenues

        #farbe ändern
        #https://stackoverflow.com/questions/6178153/how-to-change-menu-background-color-of-tkinters-optionmenu-widget
        optionmenuDesign = OptionMenu(self.Fenster, self.stringvariableStatus, *self.options)
        optionmenuDesign.config(bg="purple1")
        optionmenuDesign["menu"].config(bg="purple1")
        #endregion

        self.Fenster.mainloop()

    #region ButtonLogik
    def create_point_of_names(self,Amount):
        NameRandomizer = FullNameRandomizer(self.firstname_Collection.name_cache, self.lastname_collection.name_cache)
        NameRandomizer.Create_Multiple_random_names(Amount)
        NameRandomizer.Show_Full_Names_List()
        self.savepointOfNames.append(NameRandomizer)

    def create_point_of_emails(self,domainname,optionOfEmailStructure,seperatorkey):
        #if seperatorkey != ";":
        EmailCreator = EmailAdressCreator(self.savepointOfNames[0].Get_Namelist())
        EmailCreator.set_domain_name(domainname)
        lengthOfNamelist = len(self.savepointOfNames[0].Get_Namelist())
        if optionOfEmailStructure == "v.nachname":
            optionforEmailCreator = 1
        if optionOfEmailStructure == "vorname.nachname":
            optionforEmailCreator = 2
        if optionOfEmailStructure == "vorname.n":
            optionforEmailCreator = 3
        seperatorChar = seperatorkey
        for i in range(lengthOfNamelist):
            EmailCreator.create_email_address_name(optionforEmailCreator, self.savepointOfNames[0].Get_Namelist()[i],
                                                   seperatorChar)
            #region löschung zusätzliches_Zeichen \n - entsteht durch zusätzliche Containerisierung von objekt in Liste
            EmailCreator.set_current_Emailaddresse(str(EmailCreator.get_current_EMailaddress()).replace('\n',''))
            #endregion

            EmailCreator.create_full_email_with_current_domain_from_currentemail()
            EmailCreator.add_Current_EMailAddress_to_EmailAddressList()
        EmailCreator.show_EmailAddresseList()
        self.savepointOfEmail.append(EmailCreator)

    def create_point_of_pw(self, Amount):
        pwgen = PWGen()
        pwgen.set_passwordlength(Amount)
        self.savepointOfPW.append(pwgen)

    def create_point_of_Userzusammenfassung(self):
        userzusammenfassung = UserAdministration()
        for u in self.savepointOfEmail[-1].get_EmailAddresseList(): # -1 holt neuesten eintrag der liste (hintersten eintrag)
            self.savepointOfPW[-1].create_pw()
            userzusammenfassung.add_single_key_value_pair(u, self.savepointOfPW[-1].get_password())
        self.savepointOfZusammenfassung.append(userzusammenfassung)

    def create_csv(self):
        CSV_Builder = CSV_Creator()
        if(self.Fenster.directory != None and self.Fenster.directory != ""):
            Path = self.Fenster.directory + "/"
        else:
            Path = ""
        CSV_Builder.set_filename(Path+"EMailAdressListe")
        CSV_Builder.set_fieldnames(["Email", "Password"])
        CSV_Builder.load_source_as_dict(self.savepointOfZusammenfassung[-1].get_user_and_pw())
        CSV_Builder.build_csv_file()

    def openDir(self):
        self.Fenster.directory = filedialog.askdirectory(initialdir="/", title="Select directory")

    #endregion

    #region Statusänderungen
    def change_state_to_suche_namen(self):
        self.statustext="Status: Suche Namen..."
        return self.statustext
    def change_state_to_warte_auf_namenserstellung(self):
        self.statustext="Status: Warte auf Namenserstellung..."
        return self.statustext
    def change_state_to_erstelle_namensliste(self):
        self.statustext="Status: Erstelle Namensliste..."
        return self.statustext
    def change_state_to_warte_auf_emailadressen(self):
        self.statustext="Status: Warte auf Emailerstellung..."
        return self.statustext
    def change_state_to_erzeuge_emails(self):
        self.statustext="Status: Erzeuge Emails..."
        return self.statustext
    def change_state_to_warte_auf_passwort(self):
        self.statustext="Status: Warte auf Passwortgeneratorerstellung..."
        return self.statustext
    def change_state_to_erstelle_passwort(self):
        self.statustext="Status: Erstelle Passwortgenerator..."
        return self.statustext
    def change_state_to_warte_auf_Email_Passwoerter_Zuordnung(self):
        self.statustext="Status: Warte auf Zuordnung..."
        return self.statustext
    def change_state_to_ordne_Email_zu_Passwoerter_zu(self):
        self.statustext="Status: Ordne Emails zu Passwoerter zu..."
        return self.statustext
    def change_state_to_warte_auf_csv_erstellung(self):
        self.statustext="Status: Warte auf CSV-Erstellung..."
        return self.statustext
    def change_state_to_erstelle_csv(self):
        self.statustext="Status: Erstelle CSV..."
        return self.statustext
    def change_state_to_csv_fertig(self):
        self.statustext="Status: CSV erstellt!"
        return self.statustext
    #endregion

    #region path_state
    def change_path_state(self):
        self.pathtext = "Pfad: "
        self.pathtext = self.pathtext + self.Fenster.directory
        return self.pathtext
    #endregion

Gui = GUI_Maibaum()


