import random


class FullNameRandomizer:
    _Namelist = {}
    _FirstNameList = []
    _LastNameList = []
    publicNamelist = {}

    def __init__(self,FirstnameList,LastnameList):
        self._FirstNameList = FirstnameList
        self._LastNameList = LastnameList

    def Create_random_Name(self):
        RandomFirstname = self._FirstNameList[random.randint(0,len(self._FirstNameList)-1)]
        RandomLastname = self._LastNameList[random.randint(0, len(self._LastNameList)-1)]

        RandomName_list = [RandomFirstname, RandomLastname]
        return RandomName_list

    def Create_Multiple_random_names(self, Amount_of_Names):
        print("Nachnamen werden zusammengewürfelt...")
        for i in range(Amount_of_Names):
            self._Namelist[i] = self.Create_random_Name()
        self.publicNamelist = self._Namelist

    def Show_Full_Names_List(self):
        return print(self._Namelist)

    def Get_Namelist(self):
        return self._Namelist