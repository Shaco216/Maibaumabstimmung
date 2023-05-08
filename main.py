from FirstNameCreator import *
from LastNameCreator import *
from FullNameRandomizer import *

from EmailAdressCreator import *
from CSV_Creator import *
from PasswordGenerator import *
from UserAdministration import *

firstname_Collection = FirstNameCreator()
firstname_Collection.search_for_limited_amount_of_names(int(input("Bitte Anzahl an Vornamen beginnend bei A angeben: ")))

#print(firstname_Collection.name_cache)

lastname_collection = LastNameCreator()
lastname_collection.get_all_Last_Names()
lastname_collection.rephrase_umlauts()
#lastname_collection.show_current_result()
#print(lastname_collection.name_cache)

NameRandomizer = FullNameRandomizer(firstname_Collection.name_cache, lastname_collection.name_cache)
NameRandomizer.Create_Multiple_random_names(int(input("Bitte Anzahl an zufälligen Nachnamen angeben: ")))

#NameRandomizer.Show_Full_Names_List()
#print(NameRandomizer.Get_Namelist())

#Emailserver = EmlServer()
#Emailserver.run()

EmailCreator = EmailAdressCreator(NameRandomizer.Get_Namelist())
EmailCreator.set_domain_name(input("Bitte Name der Domäne angeben (z.B. web.de): "))
lengthOfNamelist = len(NameRandomizer.Get_Namelist())
optionforEmailCreator = int(input("Bitte zwischen folgenden Emailvariationen auswählen \n1:v.nachname\n2:vorname.nachname\n3:vorname.n\nBitte wählen Sie zwischen 1,2 und 3 aus: "))
seperatorChar = input("Bitte Trennzeichen eingeben(alles außer ;): ")
print("Emails werden generiert...")
for i in range(lengthOfNamelist):
    EmailCreator.create_email_address_name(optionforEmailCreator, NameRandomizer.Get_Namelist()[i], seperatorChar)
    EmailCreator.create_full_email_with_current_domain_from_currentemail()
    EmailCreator.add_Current_EMailAddress_to_EmailAddressList()
#User.create_email_address_name(2,NameRandomizer.Get_Namelist()[3],".")
#User.create_full_email_with_current_domain_from_currentemail()

#print(User.get_current_EMailaddress())
#print(EmailCreator.get_EmailAddresseList())

pwgen = PWGen()
useradmin = UserAdministration()
pwlen = int(input("Bitte Passwortlaenge eingeben: "))
pwgen.set_passwordlength(pwlen)
print("Passwörter werden ausgedacht...")
for u in EmailCreator.get_EmailAddresseList():
    pwgen.create_pw()
    useradmin.add_single_key_value_pair(u,pwgen.get_password())

CSV_Builder = CSV_Creator()
CSV_Builder.set_filename("EMailAdressListe")
CSV_Builder.set_fieldnames(["Email","Password"])
CSV_Builder.load_source_as_dict(useradmin.get_user_and_pw())
CSV_Builder.build_csv_file()


