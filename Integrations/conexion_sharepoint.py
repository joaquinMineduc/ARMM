from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
import time 
from functions import get_year

year = get_year().split("-")[0]
month = get_year().split("-")[1].capitalize()

print(month)
driver = webdriver.Chrome()

driver.get("https://shorturl.at/FsTEF")

time.sleep(2)

# inicio sesión

ele_input_email = driver.find_element(By.ID, "i0116").send_keys("joaquin.astorga@mineduc.cl")

ele_btn_next = driver.find_element(By.ID, "idSIButton9").click()
time.sleep(2)

ele_input_password = driver.find_element(By.ID, "i0118").send_keys("noviembre-2024")

ele_btn_login = driver.find_element(By.ID, "idSIButton9").click()
time.sleep(2)

ele_option = driver.find_element(By.ID, "idBtn_Back").click()
time.sleep(2)

# manipular carpeta ADP

button = driver.find_element(By.XPATH, "//button[@data-automationid='FieldRenderer-name' and contains(text(), 'ADP')]")
button.click()


time.sleep(2)
button = driver.find_element(By.XPATH, f"//button[@data-automationid='FieldRenderer-name' and contains(text(), '{year}')]")
button.click()

time.sleep(2)
button = driver.find_element(By.XPATH, f"//button[@data-automationid='FieldRenderer-name' and contains(text(), '{month}')]")
button.click()

time.sleep(2)

div_file = driver.find_element(By.CLASS_NAME, "ms-SelectionZone").click()

btn_download_file = driver.find_element(By.NAME, "Descargar").click()

## REPLICAR EL CODIGO ANTERIOR A RIESGOS Y PROGRAMAS SOCIALES

time.sleep(550)