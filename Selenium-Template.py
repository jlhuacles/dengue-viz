from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time
import os
import pathlib
import pandas
from datetime import datetime
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 800))  
# display.start()

dt = datetime.now()
str_time = dt.strftime("%d-%m-%Y")
thisPath = str(pathlib.Path().resolve())


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--disable-web-security",
    "--no-proxy-server",
    "--disable-blink-features=AutomationControlled"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

prefs = {
        # notifations 1= permitir 2 = no permitir 0=preguntar
        'profile.default_content_setting_values.notifications': 2,
        # Para evitar que chrome nos pregunte si queremos guardar la clave
        'credentials_enable_service': False,
        "download.default_directory" : f'{thisPath}\\archivos'
}
    
chrome_options.add_experimental_option('prefs', prefs)
def cocinarpage():
    driver.get('https://www.dge.gob.pe/sala-situacional-dengue/diaria/')
    time.sleep(3)
    wait = WebDriverWait(driver, 20)
    
    try:
        elemento = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Por distrito')]")))
    except TimeoutException:
        print("Error en elegir el elemento")
        return "Error"
    elemento.click()

    try:
        buttonDownload = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#por-distrito > div:nth-child(2) > div:nth-child(1) > a:nth-child(2)')))
    except TimeoutException:
        print("Error en elegir el button download")
        return "Error"
    buttonDownload.click()



driver = webdriver.Chrome(options = chrome_options)

driver.get('https://www.dge.gob.pe/sala-situacional-dengue/diaria/')
cocinarpage()
time.sleep(20)
driver.quit()

