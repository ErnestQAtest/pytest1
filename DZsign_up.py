from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# связь с браузером
driver = webdriver.Firefox()
# открою страничку по url адресу
url = "https://prosvirov-vladimir.github.io/test-authorization/sign-up.html"
driver.get(url)
# поиск
title = driver.find_element(By.TAG_NAME, 'h2')
print(title.text)
pointer = driver.find_element(By.ID, 'agreementChkbox')
pointer.click()
dropdown = driver.find_element(By.CLASS_NAME, 'country-dropdown')
dropdown.click()
login = driver.find_element(By.TAG_NAME, 'a')
login.click()
print(login.text)
sleep(1)

# закрою браузер
driver.quit()
