#!/usr/bin/python
#!/usr/local/bin/python

import os
import sys
import time
import platform
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options  
from tqdm import tqdm

# Link til survey
url = 'https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilmelding-til-at-modtage-overskydende-vaccine-mod-COVID-19.aspx'


#################################
#                               #
#   Skriv din information her   #
#                               #
#################################

# Skriv venligst dit fulde navn  / Full Name
fuldnavn = 'A D'

# Skriv venligst din alder / Age
alder = '30' 

# Skriv venligst din adresse (Vej, vejnummer og evt. opgang/etage) / address (street, house nr etc.)
adresse = 'mælkevejen 42 1tv'

# Skriv venligst dit postnummer og hvilken by du bor i / Zip code and city
postNrBy = '9000 aalborg'

# Bliver du udvalgt til at modtage en vaccination med en overskudsvaccine, vil du blive kontaktet telefonisk.
# Skriv derfor venligst dit telefonnummer / phone number
telefonNr = '42424242'

# Udkommenter dit vaccinationssted / Uncomment your vaccination place 
# Vælg vaccinationssted / pick vaccination place 
#vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[1]/label' # Ballerup, Baltorpvej 18
#vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[2]/label' # Bella Center, Ørestad Boulevard/Martha Christensens Vej, København S
#vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[4]/label' # Hillerød, Østergade 8
#vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[3]/label' # Bornholm, Ullasvej 39 C, Rønne
vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[5]/label' # Ishøj, Vejledalen 17
#vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[6]/label' # Øksnehallen, Halmtorvet 11, København V
#vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[7]/label' # Snekkerstenhallen, Agnetevej 1
#vaxxplace = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[8]/label' # Vaccinationscenter Birkerød, Søndervangen 44, 3460 Birkerød


# Global variables 
refreshCounter = 0
counter = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def init_Driver():

    #driver.set_window_position(895, 0)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-default-apps")
    options.add_argument("--no-first-run")
    # options.add_experimental_option("detach", True)

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    if platform.system() == 'Darwin':
        s=Service("chromedriver_osx")
    elif platform.system() == 'Windows':
        s=Service("chromedriver.exe")
    else:
        s=Service("chromedriver:linux")
        
    driver = webdriver.Chrome(options=opt) #options=options
    
    driver.set_window_size(1024, 900)

    driver.get(url)

    return driver

def autopart():
    global refreshCounter
    timer = 10#86400

    print("\nNumber of auto fills: {0}\n".format(refreshCounter))
    print("\nTime left before next auto fill\n")
    for char in tqdm(range(timer), unit='s', unit_divisor=60):
        time.sleep(1)
        #progress.set_description("Next refresh..") # 900 seconds = 15 minutes, 780s = 13 min
    refreshCounter += 1
    clear_screen()    
    submitter(url)


def submitter(url):
    driver = init_Driver()
    
    # Start survey
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click()

    # Sends full name
    fn = driver.find_element_by_name('t50100775')
    fn.send_keys(fuldnavn)

    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click() 

    # Sends age
    ald = driver.find_element_by_name('n35965768')
    ald.send_keys(alder)

    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click()

    # Sends address
    addr = driver.find_element_by_name('t50088645')
    addr.send_keys(adresse)

    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click()  

    # Sends zipcode and city    
    pby = driver.find_element_by_name('t50088674')
    pby.send_keys(postNrBy)

    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click()

    # Sends phone number
    nr = driver.find_element_by_name('n50088775')
    nr.send_keys(telefonNr)

    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click() 

    # Sends desired vaxx place
    vaxp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, vaxxplace)))
    vaxp.click() 

    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click()

    # Sends confim data
    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    nxt.click()  

    # Sends end to quit
    time.sleep(0.1)
    nxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/div[3]/input')))
    driver.close()
    # nxt.click() 
    
    autopart()

if __name__ == "__main__":
    submitter(url)
