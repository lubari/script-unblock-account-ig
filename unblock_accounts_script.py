from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
import random

USER_NAME = ""
PASSWORD = ""

# Configuración del driver
driver = webdriver.Chrome()

# Ir a instagram
sleep(2)
driver.get('https://www.instagram.com/accounts/login/')
sleep(3)

# Aceptar cookies
sleep(3)

# Entrar
username = driver.find_element(By.NAME, "username")
username.send_keys(USER_NAME)
password = driver.find_element(By.NAME, 'password')
password.send_keys(PASSWORD)

button_login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
button_login.click()
sleep(5)
print('Sesión iniciada')

driver.get('https://www.instagram.com/accounts/blocked_accounts/')
sleep(5)
blocked_accounts = driver.find_elements(By.XPATH, '//div[@aria-label="Desbloquear"]')

while blocked_accounts:
    blocked_accounts[0].click()
    sleep(5)                                  
    unblock_button2 = driver.find_element(By.XPATH, '//button[contains(@class, "_a9--") and contains(@class, "_ap36") and contains(@class, "_a9_1") and .//div[text()="Desbloquear"]]')
    unblock_button2.click()
    sleep(5)
    blocked_accounts = driver.find_elements(By.XPATH, '//div[@aria-label="Desbloquear"]')

print("No more accounts to unblock")

driver.quit()