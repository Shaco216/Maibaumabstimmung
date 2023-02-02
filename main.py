from FirstNameCreator import *
from LastNameCreator import *
from FullNameRandomizer import *

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
NameRandomizer.Show_Full_Names_List()
