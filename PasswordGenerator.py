from random import randrange

class PasswordGenerator:
    _password = ""
    _numberOfDigits = 0
    _upperCases = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    _lowerCases = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    _numbers = [0,1,2,3,4,5,6,7,8,9]
    _otherCharacters = ['!','§','$','%','&','?','/','*','-','+','#',',','.','-',';',':','_']
    _listOfAllCharacters = [_upperCases,_lowerCases,_numbers,_otherCharacters]

    def __init__(self, digits):
        self._numberOfDigits = digits

    def create_password(self, otherCharactersIncluded=False):
        if otherCharactersIncluded == True:
            numberOfSortOfCharacters = 4
            for i in range(self._numberOfDigits):
                chosenNumber = randrange(0,numberOfSortOfCharacters)
                lengthOfChosenCharacters = len(self._listOfAllCharacters[chosenNumber])
                randomCharacter = self._listOfAllCharacters[chosenNumber][randrange(0,lengthOfChosenCharacters)]
                self._password = self._password + str(randomCharacter)
        else:
            numberOfSortOfCharacters = 3
            for i in range(self._numberOfDigits):
                chosenNumber = randrange(0, numberOfSortOfCharacters )
                lengthOfChosenCharacters = len(self._listOfAllCharacters[chosenNumber])
                randomCharacter = self._listOfAllCharacters[chosenNumber][randrange(0, lengthOfChosenCharacters)]
                self._password = self._password + str(randomCharacter)

    def get_password(self):
        return self._password