from selenium import webdriver
from seleniumwire import webdriver
from seleniumwire import *
import os

class Usercreator:
    _email = ""
    _password = ""
    _driver = webdriver()

    def __init__(self, Email, Password):
        self._email = Email
        self._password = Password
        #https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ
        self._driver = webdriver.Chrome(os.getcwd()+"\chromedriver_win32\chromedriver.exe")

        #https://stackoverflow.com/questions/15645093/setting-request-headers-in-selenium
        self._driver.request_interceptor = self.interceptor(self._driver.requests)
        #start selenium

    def interceptor(self, request):
        if type(request) is list:
            newRequestList = []
            for r in request:
                del r.headers['Referer']
                r.headers['Referer'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
                newRequestList.append(r)
            return newRequestList
        elif type(request) is str:
            del request.headers['Referer']
            request.headers[
                'Referer'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            return request

    def create_Email_Account(self):
        pass