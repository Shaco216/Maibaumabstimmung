import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
from tkinter import filedialog

print('CSV bitte tabulatorgetrennt und columns in reihenfolge exakt so benannt:')
print('emailadress\tpassword\tfirstName\tlastName')

voters = []
print("Bitte CSV auswählen:")
file = filedialog.askopenfilename(filetypes='csv')
with open(file,'r') as f:
    reader = f.read()
    for line in reader:
        voters.append(line)



clicksleep = 1
typesleep = 3

emailaddress = ''
password = ''
firstName = ''
lastName = ''

driver = webdriver.Edge()  # Optional argument, if not specified will search path.

driver.get(f'https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/registrierung')
for voter in voters:
    # time.sleep(15) # Let the user actually see something!
    time.sleep(10)
    #print(driver.page_source)
    cookie = driver.find_element(By.XPATH, value="//div[@class='modal-footer']//*[@class='btn btn-secondary']")
    cookiebtn = cookie.find_element(By.XPATH, value="//*[@class='btn btn-secondary']")
    cookiebtn.click()
    time.sleep(5)
    email_box = driver.find_element(By.ID, value='femanager_field_username')
    password_box = driver.find_element(By.Id,value='femanager_field_password')
    password_repeat_box = driver.find_element(By.Id,value='femanager_field_password_repeat')
    firstName_box = driver.find_element(By.Id,value='femanager_field_firstName')
    lastName_box = driver.find_element(By.Id,value='femanager_field_lastName')
    terms_box = driver.find_element(By.Id,value='femanager_field_terms')
    submit_box = driver.find_element(By.Id,value='femanager_field_submit')

    #registrierung
    email_box.click()
    time.sleep(clicksleep)
    email_box.send_keys(emailaddress)
    time.sleep(typesleep)
    password_box.click()
    time.sleep(clicksleep)
    password_box.send_keys(password)
    time.sleep(typesleep)
    password_repeat_box.click()
    time.sleep(clicksleep)
    password_repeat_box.send_keys(password)
    time.sleep(typesleep)
    firstName_box.click()
    time.sleep(clicksleep)
    firstName_box.send_keys(firstName)
    time.sleep(typesleep)
    lastName_box.click()
    time.sleep(clicksleep)
    lastName_box.send_keys(typesleep)
    terms_box.click()
    time.sleep(clicksleep)
    submit_box.click()
    time.sleep(clicksleep)
linksAngeklickt = False
while linksAngeklickt is False:
    linksAngeklickt = input("Wurden links angeklickt? (y/n) ").lower() == 'y'
if linksAngeklickt:
    for voter in voters:
        driver.get(f'https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/voting/orte-unter-400-einwohner')
        time.sleep(10)
        votingElements = driver.find_element(By.XPATH, value="//div[@class='votingelement']")
        singelvoteElement = votingElements.find_element(By.XPATH, value="//div[@class='vote-singleimg']")
        targetElement = singelvoteElement.find_element(By.XPATH, value="//div[@data-uid=7341]")
        targetElement.click()
        time.sleep(clicksleep+4)
        submit_voting_outer_div_box = (driver.find_element(By.XPATH, value="//div[@id='c665']")
                                       .find_element(By.XPATH, value="//div[@class='ce-textpic ce-center ce-above'")
                                       .find_element(By.XPATH, value="//div[@class='ce-bodytext'"))
        submit_voting = (submit_voting_outer_div_box.find_element(By.XPATH, value="//p[@class='text-center']")
                         .find_element(By.XPATH, value="//div[@class='btn btn-primary']"))
        submit_voting.click()
        time.sleep(clicksleep)
driver.quit()