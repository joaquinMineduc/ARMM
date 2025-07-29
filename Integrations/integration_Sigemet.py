from Integrations.scrapy_functions import *

def get_reports_sigemet():
    try:
        driver = select_browser_driver()
        time.sleep(2)
        driver = create_new_conecction(driver,"https://sigemet.mineduc.cl/")
        log_in_sigemet(driver, 'joaquin.astorga', 'Hangar18@')
        time.sleep(2)
        driver = create_new_conecction(driver, "https://sigemet.mineduc.cl/cmi/index.jsp")
        download_report_indicators(driver)
        time.sleep(2)
        download_eval_prov(driver)
    except:
        print("Hay un error en la conexión o no se ha encontrado el elemento en la web")
        driver.close()
        driver.quit()
        


