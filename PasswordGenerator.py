import random
class PWGen:
    _alphabet = "abcdefghijklmnopqrstuvwxyz"
    _numbers = "0123456789"
    _rest = "!§$%&/()=?{[]}*-+#,.-:_~<>"
    _pw = ""
    _allCharacters = False
    _onlyNumbersAndUpperLowerAlphabet = False
    _onlyLowerandUpperAlphabet = False
    _onlyLowerAlphabet = False
    _passwordpool = ""

    def __init__(self, allCharacters = True, onlyNumbersAndUpperLowerAlphabet = False, onlyLowerandUpperAlphabet = False, onlyLowerAlphabet = False):
        self._allCharacters = allCharacters
        self._onlyNumbersAndUpperLowerAlphabet = onlyNumbersAndUpperLowerAlphabet
        self._onlyLowerandUpperAlphabet = onlyLowerandUpperAlphabet
        self._onlyLowerAlphabet = onlyLowerAlphabet
        if(self._onlyNumbersAndUpperLowerAlphabet):
            self._passwordpool = self._passwordpool.replace(self._rest)
        elif(self._onlyLowerandUpperAlphabet):
            self._passwordpool = self._passwordpool.replace(self._rest+self._numbers)
        elif(self._onlyLowerAlphabet):
            self._passwordpool = self._alphabet
        else:
            self._passwordpool = self._alphabet + self._alphabet.upper() +self._numbers +self._rest

    def change_passwordpool(self):
        if(self._onlyNumbersAndUpperLowerAlphabet):
            self._passwordpool = self._passwordpool.replace(self._rest)
        elif(self._onlyLowerandUpperAlphabet):
            self._passwordpool = self._passwordpool.replace(self._rest+self._numbers)
        elif(self._onlyLowerAlphabet):
            self._passwordpool = self._alphabet

    def create_pw(self,lengthOfPw):
        self._pw = ""
        for i in range(lengthOfPw):
            #print(len(self._passwordpool))
            self._pw = self._pw + self._passwordpool[random.randint(0,len(self._passwordpool)-1)]

    def get_password(self):
        return self._pw
