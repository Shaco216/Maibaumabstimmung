import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
from tkinter import filedialog
from voter import voteuser
import tkinter as tk
from tkinter import *
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

print('CSV bitte kommagetrennt und columns in reihenfolge exakt so benannt:')
print('emailadress,password,firstName,lastName')

voters = []
print("Bitte CSV auswählen:")
file = filedialog.askopenfilename(title = "Select CSV-File",filetypes = (("CSV Files","*.csv"),))
with open(file,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        voterino = voteuser(emailaddress=str(line[0]),password=str(line[1]),vorname=str(line[2]),nachname=str(line[3]))
        print(voterino)
        voters.append(voterino)

clicksleep = 1
typesleep = 3

# emailaddress = ''
# password = ''
# firstName = ''
# lastName = ''

options = Options()

# options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge Beta\Application\msedge.exe"
# driver = webdriver.Edge(options = options)
# driver = webdriver.Firefox()
driver = webdriver.Edge()  # Optional argument, if not specified will search path.
driver.maximize_window()
seitenaufbauZeit = 10

root = tk.Tk()
root.attributes("-topmost", True)
startlabel = Label(root,text="Aktion ist in Terminal erforderlich")
startlabel.pack()
startproceed = Button(root,command=root.destroy, text="Ok")
startproceed.pack()
root.mainloop()

regErledigtBool = input("Wurde Registrierung bereits erledigt? (y/n) ").lower() == 'y'
cookiesAkzeptiert = False
time.sleep(10)
if regErledigtBool == False:
    for voteri in voters:
        driver.get(f'https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/registrierung')
        # time.sleep(15) # Let the user actually see something!
        time.sleep(seitenaufbauZeit)
        #print(driver.page_source)
        try:
            if cookiesAkzeptiert is False:
                cookie = driver.find_element(By.XPATH, value="//div[@class='modal-footer']//*[@class='btn btn-secondary']")
                cookiebtn = cookie.find_element(By.XPATH, value="//*[@class='btn btn-secondary']")
                cookiebtn.click()
                cookiesAkzeptiert = True
                time.sleep(5)
        except Exception as e:
            print(e)
        email_box = driver.find_element(By.ID, value='femanager_field_username')
        password_box = driver.find_element(By.ID,value='femanager_field_password')
        password_repeat_box = driver.find_element(By.ID,value='femanager_field_password_repeat')
        firstName_box = driver.find_element(By.ID,value='femanager_field_firstName')
        lastName_box = driver.find_element(By.ID,value='femanager_field_lastName')
        terms_box = driver.find_element(By.ID,value='femanager_field_terms')
        submit_box = driver.find_element(By.ID,value='femanager_field_submit')

        #registrierung
        email_box.click()
        time.sleep(clicksleep)
        email_box.send_keys(voteri.emailaddress)
        time.sleep(typesleep)
        driver.execute_script("arguments[0].scrollIntoView();", password_box)
        password_box.click()
        time.sleep(clicksleep)
        password_box.send_keys(voteri.password)
        time.sleep(typesleep)
        driver.execute_script("arguments[0].scrollIntoView();", password_repeat_box)
        password_repeat_box.click()
        time.sleep(clicksleep)
        password_repeat_box.send_keys(voteri.password)
        time.sleep(typesleep)
        driver.execute_script("arguments[0].scrollIntoView();", firstName_box)
        firstName_box.click()
        time.sleep(clicksleep)
        firstName_box.send_keys(voteri.vorname)
        time.sleep(typesleep)
        driver.execute_script("arguments[0].scrollIntoView();", lastName_box)
        lastName_box.click()
        time.sleep(clicksleep)
        lastName_box.send_keys(voteri.nachname)
        time.sleep(typesleep)
        driver.execute_script("arguments[0].scrollIntoView();", terms_box)
        time.sleep(1)
        terms_box.click()
        time.sleep(clicksleep)
        driver.execute_script("arguments[0].scrollIntoView();", submit_box)
        time.sleep(1)
        submit_box.click()
        time.sleep(clicksleep)
        print(voterino.emailaddress + ' wurde angelegt.')
        try:
            driver.get(f'https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/registrierung')
            time.sleep(seitenaufbauZeit)
            abmeldebutton_region = driver.find_element(By.ID, value="c600")
            abmeldebutton = abmeldebutton_region.find_element(By.XPATH, value="//input[@value='Abmelden']")
            driver.execute_script("arguments[0].scrollIntoView();", abmeldebutton)
            abmeldebutton.click()
            print(voterino.emailaddress + 'wurde abgemeldet.')
            time.sleep(clicksleep)
        except Exception as e:
            print(e)
    regErledigtinput = True

if regErledigtBool:
    linksAngeklickt = False

    root = tk.Tk()
    root.attributes("-topmost", True)
    startlabel = Label(root, text="Aktion ist in Terminal erforderlich")
    startlabel.pack()
    startproceed = Button(root, command=root.destroy, text="Ok")
    startproceed.pack()
    root.mainloop()

    while linksAngeklickt is False:
        linksAngeklickt = input("Wurden links angeklickt? (y/n) ").lower() == 'y'
    time.sleep(10)
    if linksAngeklickt:
        for voteri in voters:
            driver.get(f'https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/registrierung')
            time.sleep(seitenaufbauZeit)
            try:
                if cookiesAkzeptiert is False:
                    cookie = driver.find_element(By.XPATH,
                                                 value="//div[@class='modal-footer']//*[@class='btn btn-secondary']")
                    cookiebtn = cookie.find_element(By.XPATH, value="//*[@class='btn btn-secondary']")
                    cookiebtn.click()
                    cookiesAkzeptiert = True
                    time.sleep(5)
            except Exception as e:
                print(e)
            anmeldung = driver.find_element(By.ID, value="c600")
            anmeldung_form = anmeldung.find_element(By.XPATH, value="//form[@target='_top']")
            anmeldung_input_name = anmeldung_form.find_element(By.XPATH, value="//input[@name='user']")
            driver.execute_script("arguments[0].scrollIntoView();", anmeldung_input_name)
            anmeldung_input_name.click()
            time.sleep(clicksleep)
            anmeldung_input_name.send_keys(voteri.emailaddress)
            time.sleep(typesleep)
            anmeldung_input_pass = anmeldung_form.find_element(By.XPATH, value="//input[@name='pass']")
            anmeldung_input_pass.click()
            time.sleep(clicksleep)
            anmeldung_input_pass.send_keys(voteri.password)
            time.sleep(typesleep)
            anmeldeButton = anmeldung_form.find_element(By.XPATH, value="//input[@value='Anmelden']")
            driver.execute_script("arguments[0].scrollIntoView();", anmeldeButton)
            anmeldeButton.click()
            time.sleep(clicksleep)
            driver.get(f'https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/voting/orte-unter-400-einwohner')
            time.sleep(seitenaufbauZeit)
            votingElements = driver.find_element(By.XPATH, value="//div[@class='votingelement']")
            singelvoteElement = votingElements.find_element(By.XPATH, value="//div[@class='vote-singleimg']")
            #driver.execute_script("arguments[0].scrollIntoView();", singelvoteElement)
            #time.sleep(3)
            print(singelvoteElement.text)
            targetElement = singelvoteElement.find_element(By.XPATH, value="//span[@data-uid=7341]")
            print(targetElement.text)
            driver.execute_script("arguments[0].scrollIntoView();", targetElement)

            time.sleep(5)
            targetElement.click()
            print("Element wurde geklickt")
            time.sleep(clicksleep+4)
            content0 = driver.find_element(By.XPATH, value="content0 container")
            DIVc665 = content0.find_element(By.ID, value="c665")
            submit_overbox = DIVc665.find_element(By.XPATH, value="//div[@class='ce-textpic ce-center ce-above'")
            submit_under_overbox = submit_overbox.find_element(By.XPATH, value="//div[@class='ce-bodytext'")
            submit_voting = (submit_under_overbox.find_element(By.XPATH, value="//p[@class='text-center']")
                             .find_element(By.XPATH, value="//div[@class='btn btn-primary']"))
            driver.execute_script("arguments[0].scrollIntoView();", submit_voting)
            submit_voting.click()
            time.sleep(clicksleep)
            try:
                driver.get(f'https://www.schlossbrauerei-unterbaar.de/maibaum-aktion/registrierung')
                time.sleep(seitenaufbauZeit)
                abmeldebutton_region = driver.find_element(By.ID, value="c600")
                abmeldebutton = abmeldebutton_region.find_element(By.XPATH, value="//input[@value='Abmelden']")
                driver.execute_script("arguments[0].scrollIntoView();", abmeldebutton)
                abmeldebutton.click()
                time.sleep(clicksleep)
            except Exception as e:
                print(e)
driver.quit()
