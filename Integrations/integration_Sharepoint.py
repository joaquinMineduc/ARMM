from scrapy_functions import *
from selenium.webdriver.chrome.options import Options



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

upload_reportBI()