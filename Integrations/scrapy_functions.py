from datetime import datetime
import time 
import locale
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    WebDriverException,
    SessionNotCreatedException,
    TimeoutException,
    NoSuchDriverException,
    InvalidArgumentException,
    UnexpectedAlertPresentException
)

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
    else:
        year = datetime.now().year
    date = datetime(year, month, 1).strftime("%Y-%B")
    return date

year = get_year().split("-")[0]

month = get_year().split("-")[1].capitalize()



def select_browser_driver():
    browsers = ["chrome", "firefox", "edge"] 
    driver = None
    
    for browser in browsers:
        try:
            if browser == "edge":
                driver = webdriver.Edge()
            elif browser == "firefox":
                driver = webdriver.Firefox()
            elif browser == "chrome":
                driver = webdriver.Chrome()
            return driver
        except (SessionNotCreatedException, NoSuchDriverException):
            # alguna función que envíe un mensaje al usuario
            print("error")
        except (WebDriverException, TimeoutException, InvalidArgumentException):
            # alguna función que envíe un mensaje al usuario
            print("error")


def create_new_conecction(driver, url):
    try:
        driver.get(url)
    except (TimeoutException):
        print("Se ha agotado el tiempo de respuesta de la página")
        driver.refresh()
    except InvalidArgumentException:
        print("la url proporcionada es inválida, se recomienda verificar la url")
    except UnexpectedAlertPresentException:
        print("La ventana del navegador no existe, reiniciando WebDriver...")
        driver.quit()
        driver = select_browser_driver()
        driver.get(url)
    except WebDriverException:
        print("Error general, reiniciando WebDriver...")
        driver.quit()
        driver = select_browser_driver()
        driver.get(url)
    return driver

def log_in_sharepoint(driver, email, password):
    time.sleep(2)
    driver.find_element(By.ID, "i0116").send_keys(email)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)
    driver.find_element(By.ID, "i0118").send_keys(password)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)
    driver.find_element(By.ID, "idBtn_Back").click()
    time.sleep(2)
    return driver


def back_directory_base(driver):
    for i in range (3):
        driver.back()
    driver.refresh()
    

def get_document(driver, name_file):
    try:
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[@role='button'"+
            f"and contains(text(), '{name_file}')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@role='button' and @data-id='heroField'"+
            f" and @data-selection-invoke='true' and contains(text(), '{year}')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@role='button' and @data-id='heroField'"+
            f" and @data-selection-invoke='true' and contains(text(), '{month}')]").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "rowSelectionCell_eed5868f  ").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@title='Más acciones'"+
            " and @aria-label='Más acciones' and @data-automationid='moreActionsHeroField'"+
            " and @data-selection-invoke='true']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@data-automationid='downloadCommand'"+
            " and @role='menuitem']//span[contains(text(), 'Descargar')]").click()
        time.sleep(2)
    except:
        print("Verificar que los directorios no hayan sido modificados"+ 
              "y que la planilla excel se encuentra en su respectiva carpeta")


# esta  función permite iniciar sesión en sigemet      
def log_in_sigemet(driver, user, password):
    driver.switch_to.frame("seccion")
    principal_frame = driver.find_element(By.ID, "seccionFrameset")
    principal_frame.find_element(By.NAME, "cuerpo")
    driver.switch_to.frame("cuerpo")
    second_frame = driver.find_element(By.ID, "cuerpo_seccion")
    second_frame.find_element(By.NAME, "mainFrame")
    driver.switch_to.frame("mainFrame")
    
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME, "passwdTxt").send_keys(password)
    driver.find_element(By.NAME, "commit").click()
    
# verificar si es necesario guardar el elemento en variables, si no lo es, mejorar mediante ciclos
def go_management_instruments(driver):
    elements = [
        "frameset", "seccion", "seccionFrameset", "menu", "link_3", "cuerpo",
        "frameset", "cambio_subcategoria", "cuerpo_seccion", "leftFrame", "linkItem_16190",
        "frame", "mainFrame", "considerarAplicacionesReg", "botonXls"
    ]

    for element in elements:
        if element == "frameset":
            driver.find_element(By.TAG_NAME, element)  # Find the frameset tag
        elif element in ["seccion", "menu", "cuerpo", "cambio_subcategoria", "leftFrame"]:
            driver.switch_to.frame(element)  # Switch to frames
        elif element in ["link_3", "linkItem_16190"]:
            driver.find_element(By.ID, element).click()
            time.sleep(2)
            driver.switch_to.parent_frame()
        else:
            driver.find_element(By.ID, element)  # Find other elements
        time.sleep(1)  # Optional delay for stability
    time.sleep(5)  # Final delay after all actions
    
    
 





# verifica si el   
def verify_directory(drive, element):
    if element:
        pass
    else:
        pass
        
    
    

