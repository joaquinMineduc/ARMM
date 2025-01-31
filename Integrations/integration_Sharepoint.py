from scrapy_functions import *

def get_instruments_files():
    # Inicio sesión en Sharepoint y descarga documento ADP
    driver = select_browser_driver()
    driver = create_new_conecction(driver,"https://shorturl.at/FsTEF")
    driver = log_in_sharepoint(driver, "joaquin.astorga@mineduc.cl", "noviembre-2024")
    get_document(driver, 'ADP')

    # retroceder a inicio y descargar documento gestión de riesgos
    back_directory_base(driver)
    get_document(driver, 'Gestión de Riesgos')

    #retroceder al inicio y descargar documento programas sociales
    back_directory_base(driver)
    get_document(driver, 'Programas sociales')
    
def upload_reportBI():
    pass

def download_reportsBI():
    pass

def merge_and_upload_reportBI():
    pass

get_instruments_files()