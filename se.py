from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "https://makarova1507ana.github.io/registration_page/"
driver.get(url)
sleep(5)
# coding_shmoding
driver.quit()