from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time
import os
import pathlib
import pandas
from datetime import datetime


dt = datetime.now()
str_time = dt.strftime("%d-%m-%Y")



def iniciar_chrome():
    ruta = ChromeDriverManager(path='./chromedriver').install()
    thisPath = str(pathlib.Path().resolve())
    options = Options()
    options.add_argument("--window-size=1920,1080")  # tamaño de ventana
    # deshabilita la politica del mismo origin
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")  # deshabilita extensiones
    # deshabilita las notificaciones
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")  # deshabilita el modo sandbox
    # chrome no muestra nada en la terminal
    options.add_argument("--log-level=3")
    # desactiva el aviso de "contenido seguro"
    options.add_argument("--allow-running-insecure-content")
    # desactiva el aviso de que Chromer no es el navegador por defecto
    options.add_argument("--no-default-browser-check")
    # desactiva el aviso de tareas que se hacen por primera vez
    options.add_argument("--no-first-run")
    # mencionando que usamos conexiones directas y no proxys
    options.add_argument("--no-proxy-server")
    # evita que selenium sea detectado con js
    options.add_argument("--disable-blink-features=AutomationControlled")
    exp_opt = [
        # ya no mostrará "un software automatizado de pruebas está controlando"
        'enable-automation',
        'ignore-certificate-erros',
        'enable-logging',  # para que no se muestren los mensajes de chromedrive en la terminal
    ]
    # se añade la lista de parametros a omitir
    options.add_experimental_option("excludeSwitches", exp_opt)
    # Preferencias
    prefs = {
        # notifations 1= permitir 2 = no permitir 0=preguntar
        'profile.default_content_setting_values.notifications': 2,
        # definir idiomas del navegador
        'intl.accept_languages': ['es-ES', 'es'],
        # Para evitar que chrome nos pregunte si queremos guardar la clave
        'credentials_enable_service': False,
        "download.default_directory" : f'{thisPath}\\archivos'
    }
    
    options.add_experimental_option('prefs', prefs)

    s = Service(ruta)
    driver = webdriver.Chrome(service = s, options = options)
    driver.set_window_position(0,0)
    return driver

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


def rename_and_date():
    dt = datetime.now()
    str_time = dt.strftime("%d-%m-%Y-%H-%M-%S")
    os.rename("./archivos/indicadores_dengue_diario_distrito.xlsx", f"./archivos/dengue-diario-{str_time}.xlsx")   
    

if __name__ == '__main__':
    driver = iniciar_chrome()
    res = cocinarpage()
    time.sleep(10)

    # try:
    #     file = open("./archivos/indicadores_dengue_diario_distrito.xlsx")
    #     file.close()
    # except FileNotFoundError:
    #     print("No se pudo abrir el archivo")
    #     exit()
    # finally:
    #     rename_and_date()

  
    driver.quit()
    
    