import random
import string


class EmailAdressCreator:
    namelist = []
    EmailAddressList = []
    options = {"f.lastname":1,"firstname.lastname":2,"firstname.l":3}
    currentEmailaddress = ""
    Availability_current_EMail_Address = False
    domainname = ""
    EMaillist_with_domainname = []
    def __init__(self,namelist):
        self.namelist = namelist

    def add_name_to_namelist(self, name):
        self.namelist.append(name)
    def set_domain_name(self):
        self.domainname = input("Please enter Domainname: ")
    def create_full_email_with_current_domain_from_currentemail(self):
        if self.domainname != "" and self.currentEmailaddress != "":
            self.currentEmailaddress = self.currentEmailaddress + "@" + self.domainname
    def create_full_email_with_current_domain(self, EMailaddress):
        if self.domainname != "":
            self.currentEmailaddress = EMailaddress + "@" + self.domainname
    def show_namelist(self):
        return self.namelist

    def add_EMailAddress_to_EmailAddressList(self, EMailAddress):
        self.EmailAddressList.append(EMailAddress)

    def add_Current_EMailAddress_to_EmailAddressList(self):
       self.EmailAddressList.append(self.currentEmailaddress)

    def get_current_EMailaddress(self):
        return self.currentEmailaddress

    def create_email_address_name(self, option, Namecombination, seperator):
        firstname = Namecombination[1]
        lastname = Namecombination[2]
        if option == 1:
            EmailAddress = firstname[1]+seperator+lastname
        elif option == 2:
            EmailAddress = firstname+seperator+lastname
        elif option == 3:
            EmailAddress = firstname + seperator + lastname[1]
        self.currentEmailaddress = EmailAddress

    def set_randomized_if_ascii_number_puctuation(self):
        ascii_number_puctuation = random.randint(1, 9)
        if ascii_number_puctuation < 4:
            result = string.ascii_letters
        elif ascii_number_puctuation > 6:
            result = string.punctuation
        else:
            result = string.digits
        return result
    def expand_email_address_name(self, EMailAddress):
        randomchar = random.choice(self.set_randomized_if_ascii_number_puctuation())
        EMailAddress = EMailAddress+randomchar
        self.currentEmailaddress = EMailAddress

    def exchange_last_character_of_Email_address(self, EMailAddress):
        lenght_to_second_last_digit = 2
        emailname = EMailAddress[0:len(EMailAddress)-lenght_to_second_last_digit]
        self.expand_email_address_name(emailname)
