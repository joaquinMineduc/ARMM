from scrapy_functions import *
from selenium.webdriver.chrome.options import Options
from pywinauto import Application
import os
from pathlib import Path
from pywinauto.keyboard import send_keys

def get_instruments_files():
    # Inicio sesión en Sharepoint y descarga documento ADP
    driver = select_browser_driver()
    driver = create_new_conecction(driver,"https://shorturl.at/FsTEF")
    driver = log_in_sharepoint(driver, "armm.dpcg.system@mineduc.cl", "ERMC$7835*$")
    # Encuentra los elementos dentro de gridItemFocusFrame
    get_document(driver, 'ADP')
    back_directory_base(driver)
    # retroceder a inicio y descargar documento gestión de riesgos
    get_document(driver, 'Gestión de Riesgos')
    #retroceder al inicio y descargar documento programas sociales
    back_directory_base(driver)
    get_document(driver, 'Programas sociales')
    driver.close()
    driver.quit()
    
def upload_reportBI():
    # Inicio sesión en Sharepoint y descarga documento ADP
    driver = select_browser_driver()
    driver = create_new_conecction(driver,"https://shorturl.at/FsTEF")
    driver = log_in_sharepoint(driver, "armm.dpcg.system@mineduc.cl", "ERMC$7835*$")
    get_document(driver, 'Acumulativos BI')

def download_reportsBI():
    pass

def merge_and_upload_reportBI():
    pass

#upload_reportBI()

def de_prueba():
 
    ruta_archivo = "C:/Users/joaquin.astorga/mis_proyectos/Proyecto ARMM"
    name_file = "datosBI_diciembre.xlsx"
  
    driver = select_browser_driver()
    driver = create_new_conecction(driver,"https://shorturl.at/FsTEF")
    driver = log_in_sharepoint(driver, "armm.dpcg.system@mineduc.cl", "ERMC$7835*$")
    driver.find_element(By.XPATH, "//span[@role='button'"+
            f"and contains(text(), 'Acumulativos BI')]").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "container_a4f5cb66").click()
    wait = WebDriverWait(driver, 4) 
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automationid="newFolderCommand"]'))).click()
    time.sleep(2)
    # Seleccionar la segunda opción (índice 1 porque empieza en 0)
    driver.find_element(By.ID, "textField4").send_keys("2025")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation-id="Crear"]'))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[@role='button'"+
            f"and contains(text(), '2025')]").click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automationid="uploadCommand"]'))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automationid="uploadFileCommand"]'))).click()
    time.sleep(5)

        # Connect to the Open File dialog
    app = Application().connect(title_re=".*Abrir.*")
    window = app.window(title_re=".*Abrir.*")

    # Locate the toolbar where the path is shown
    toolbar = window.child_window(title_re="Dirección:.*", class_name="ToolbarWindow32")
    # Click the toolbar
    toolbar.click_input()

    # Select all text (Ctrl + A) and delete
    send_keys("^a{DEL}")

    # Type the new path
    send_keys(ruta_archivo.replace(" ", "{SPACE}"))

    # Press Enter
    send_keys("{ENTER}")
    
    file_name_input = window.child_window(class_name="Edit", found_index=0)  
    file_name_input.set_text(name_file)
    time.sleep(2)
    open_button = window.child_window(class_name="Button", found_index=0)
    open_button.click()
    
    time.sleep(10)
    

de_prueba()





