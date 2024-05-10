
class voteuser:
    emailaddress = ""
    password = ""
    vorname = ""
    nachname = ""
    def __init__(self, emailaddress, password, vorname, nachname):
        self._emailaddress = emailaddress
        self._password = password
        self._vorname = vorname
        self._nachname = nachname