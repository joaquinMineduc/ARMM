from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 


driver = webdriver.Chrome()
driver.get("https://dev.arbol-logika.com/cmi-mineduc/")

# cuando hay frames impiden el ingreso a los objetos dentro de el, para esto debe cambiar de frame

driver.switch_to.frame("seccion")

principal_frame = driver.find_element(By.ID, "seccionFrameset")

frame = principal_frame.find_element(By.NAME, "cuerpo")

driver.switch_to.frame("cuerpo")

second_frame = driver.find_element(By.ID, "cuerpo_seccion")

frame2 = second_frame.find_element(By.NAME, "mainFrame")

driver.switch_to.frame("mainFrame")

input_user = driver.find_element(By.NAME, "login").send_keys("control")

input_password = driver.find_element(By.NAME, "passwdTxt").send_keys("1234")

btn_submit = driver.find_element(By.NAME, "commit").click()

# -- Ingreso a moduo instrumentos de gestión
driver.get("https://dev.arbol-logika.com/cmi-mineduc/index.jsp")

frame_set = driver.find_element(By.TAG_NAME, "frameset")

frame_body = frame_set.find_element(By.NAME, "seccion")

driver.switch_to.frame("seccion")

frame_set2 = driver.find_element(By.ID, "seccionFrameset")

# selección de opciones

driver.switch_to.frame("menu")

option_menu = driver.find_element(By.ID, "link_3").click()

driver.switch_to.parent_frame()

driver.switch_to.frame("cuerpo")

frame_set_principal = driver.find_element(By.TAG_NAME, "frameset")

frame_principal = frame_set_principal.find_element(By.NAME, "cambio_subcategoria")

driver.switch_to.frame("cambio_subcategoria")

frame_set_body = driver.find_element(By.ID, "cuerpo_seccion")

frame_selection = frame_set_body.find_element(By.NAME, "leftFrame")

driver.switch_to.frame("leftFrame")

ind_servicio = driver.find_element(By.ID, "linkItem_16190").click()

# modulo indicadores del servicio

driver.switch_to.parent_frame()

iframes = driver.find_elements(By.TAG_NAME, "frame")

driver.switch_to.frame("mainFrame")

wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos
checkbox = wait.until(EC.presence_of_element_located((By.ID, "considerarAplicacionesReg"))).click()

btn_download_report = wait.until(EC.presence_of_element_located((By.ID, "botonXls"))).click()

time.sleep(2)
# descargar evaluación de proveedores 

driver.switch_to.parent_frame()

driver.switch_to.frame("leftFrame")

option_eval_internal = driver.find_element(By.ID, "linkItem_17175").click()

driver.switch_to.parent_frame()

iframes = driver.find_elements(By.TAG_NAME, "frame")

for iframe in iframes:
    print(iframe.get_attribute("name"))

driver.switch_to.frame("mainFrame")

select_period =  wait.until(EC.presence_of_element_located((By.ID, "periodo")))

# Convertirlo en un objeto Select
select = Select(select_period)


# Seleccionar por índice (empieza desde 0)
select.select_by_index(0)

time.sleep(1)
download_eval_report = driver.find_element(By.ID, "btnExportExcel").click()



time.sleep(240)
