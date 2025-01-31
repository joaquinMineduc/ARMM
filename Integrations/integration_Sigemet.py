from scrapy_functions import *

driver = select_browser_driver()
driver = create_new_conecction(driver,"https://dev.arbol-logika.com/cmi-mineduc/")
log_in_sigemet(driver, 'control', '1234')
driver = create_new_conecction(driver, "https://dev.arbol-logika.com/cmi-mineduc/index.jsp")
go_management_instruments(driver)