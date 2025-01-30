from datetime import datetime
import locale
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 

# Configuración del idioma del entorno local, se cambia de EN a ES
try:
    # Esto funciona en la mayoría de los sistemas operativos
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para sistemas basados en Unix/Linux
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Para Windows


def get_year():
    month = datetime.now().month -1
    if month == 0:
        month = 12
        year = datetime.now().year -1
    date = datetime(year, month, 1).strftime("%Y-%B")
    return date


def select_browser(driver):
    match driver:
        case 1:
            driver = webdriver.Chrome()
        case 2:
            driver = webdriver.Firefox()
        case 3:
            driver = webdriver.Edge()
        case _:
            driver = webdriver.Safari()
    return driver

    
    


