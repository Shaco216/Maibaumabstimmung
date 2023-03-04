from FirstNameCreator import *
from LastNameCreator import *
from FullNameRandomizer import *
from EMailServer import *
from EmailAdressCreator import *
from PasswordGenerator import *
from UserCreator import *

firstname_Collection = FirstNameCreator()
firstname_Collection.search_for_limited_amount_of_names(30)
#print(firstname_Collection.name_cache)

lastname_collection = LastNameCreator()
lastname_collection.get_all_Last_Names()
lastname_collection.rephrase_umlauts()
#lastname_collection.show_current_result()
#print(lastname_collection.name_cache)

NameRandomizer = FullNameRandomizer(firstname_Collection.name_cache, lastname_collection.name_cache)
NameRandomizer.Create_Multiple_random_names(10)
#NameRandomizer.Show_Full_Names_List()


#Emailserver = EmlServer()
#Emailserver.run()

Emailaccount = EmailAdressCreator(NameRandomizer.Get_Namelist())
Emailaccount.set_domain_name("newMail.com")
Emailaccount.create_email_address_name(2, NameRandomizer.Get_Namelist()[3], ".")
Emailaccount.create_full_email_with_current_domain_from_currentemail()
print(Emailaccount.get_current_EMailaddress())

PasswordGen = PasswordGenerator(18)
PasswordGen.create_password(otherCharactersIncluded=False)
print(PasswordGen.get_password())


