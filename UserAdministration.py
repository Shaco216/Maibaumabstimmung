import random

class UserAdministration:
    _userAndPW = {}

    def __init__(self):
        pass
    def create_userAndPWDict(self, userlist, pwlist):
        res = {}
        for key in userlist:
            for value in pwlist:
                res[key] = value
                pwlist.remove(value)
                break
        self._userAndPW = res
    def add_single_key_value_pair(self, key, value):
        self._userAndPW.update({key:value})
    def get_user_and_pw(self):
        return self._userAndPW