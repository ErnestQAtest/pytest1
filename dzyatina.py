from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import *

brows = webdriver.Firefox()
url = "https://makarova1507ana.github.io/registration_page/"
brows.get(url)
sleep(1)

input_firstN = brows.find_element(By.ID, 'fname')
input_lustN = brows.find_element(By.ID, 'lname')
input_mail = brows.find_element(By.ID, 'email')
radio_gen = brows.find_element(By.ID, 'male')
input_date = brows.find_element(By.ID, 'birthday')
input_phone = brows.find_element(By.ID, 'phone')
input_password = brows.find_element (By.ID, 'password')
input_dropdown_country = Select(brows.find_element_by_id("country"))
# И     даже пробвал dropdown_country = Select(brows.find_element(By.ID, "country"))
input_firstN.click()
input_firstN.send_keys('brahmaputra')

input_lustN.click()
input_lustN.send_keys('avalokataishvar')

input_mail.click()
input_mail.send_keys('pochta@testovaya.00')

radio_gen.click()

brows.quit()