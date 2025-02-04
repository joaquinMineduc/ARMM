from scrapy_functions import *

driver = select_browser_driver()
driver = create_new_conecction(driver,"http://sigemet.mineduc.cl/cmi/index.jsp")
log_in_sigemet(driver, 'joaquin.astorga', 'Hangar18@')
driver = create_new_conecction(driver, "https://dev.arbol-logika.com/cmi-mineduc/index.jsp")
download_report_indicators(driver)
download_eval_prov(driver)