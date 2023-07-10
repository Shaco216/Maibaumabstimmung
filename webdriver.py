from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import *
from webdriver_manager.chrome import ChromeDriverManager

#region UserData
username = ""
password = ""
firstname = ""
lastname = ""
steet = ""
housenumber = 0
PLZ = 0
town = ""
telephone = 0
#endregion


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#driver.get(r"https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/voting-2023/orte-unter-400-einwohner")
driver.get(r"https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/registrierung")

#region fill registration
Fuser = driver.find_element(By.ID, 'femanager_field_username')
Fpw1 = driver.find_element(By.ID, 'femanager_field_password')
Fpw2 = driver.find_element(By.ID, 'femanager_field_password_repeat')
FfirstN = driver.find_element(By.ID, 'femanager_field_firstName')
FlastN = driver.find_element(By.ID, 'femanager_field_lastName')
Faddress = driver.find_element(By.ID, 'femanager_field_address')
Fplz = driver.find_element(By.ID, 'femanager_field_zip')
Fcity = driver.find_element(By.ID, 'femanager_field_city')
Ftelephone = driver.find_element(By.ID, 'femanager_field_telephone')


Fuser.send_keys(username)
#endregion
driver.quit()