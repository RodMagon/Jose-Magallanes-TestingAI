from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import datetime
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('prefs', {
    'profile.default_content_setting_values.notifications': 2,  # Deshabilitar notificaciones
    'profile.default_content_setting_values.geolocation': 2,   # Denegar acceso a la ubicación
    'profile.default_content_setting_values.camera': 2,         # Denegar acceso a la cámara
    'profile.default_content_setting_values.microphone': 2,     # Denegar acceso al micrófono
 
})
driver = webdriver.Chrome(options = options)

try:
	driver.get("https://demoqa.com/login")
	driver.implicitly_wait(30)

	print('Start the Program')
	driver.maximize_window()
	element = driver.find_element(By.XPATH, '//input[@id="userName"]')
	element.send_keys("testQAProyect")
	element = driver.find_element(By.XPATH, '//input[@id="password"]')
	element.send_keys("Maxi001$")
	time.sleep(5)
	element = driver.find_element(By.XPATH, '//button[@id="login"]')
	element.click() 
	time.sleep(5)
except Exception as e:
	print("*****************Detalle de la excepcion******************: ", str(e))


#finally:
	#driver.close()

