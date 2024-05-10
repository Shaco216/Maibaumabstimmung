
class voteuser:
    emailaddress = ""
    password = ""
    vorname = ""
    nachname = ""
    def __init__(self, emailaddress, password, vorname, nachname):
        self.emailaddress = emailaddress
        self.password = password
        self.vorname = vorname
        self.nachname = nachname