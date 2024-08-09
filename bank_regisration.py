# тест-кейс создания пользователя на странице - https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust
# 1. открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust
# 2. нажать на поле "First Name"
# 3. ввести в поле "First Name" данные - "Kirill"
# 4. нажать на поле "Last Name"
# 5. ввести в поле "Last Name" данные - "T"
# 6. нажать на поле "Post Code"
# 7. ввести в поле "Post Code" данные - "BF7117)"
# 8. нажать на кнопку "Add Customer"
# Ожидаемый результат - создается пользователь с введенными данными

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"
    driver.get(url)
    yield driver

def test_bank_add_customer(driver):
    driver.implicitly_wait(10)
    first_name_input = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')
    last_name_input = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')
    post_code_input = driver.find_element(By.XPATH, '//input[@placeholder="Post Code"]')
    add_button = driver.find_element(By.CLASS_NAME, 'btn.btn-default')
    l_name = "Kirill"
    s_name = "T"
    p_code = "BF7117"

    first_name_input.click()
    first_name_input.clear()
    first_name_input.send_keys(l_name)

    last_name_input.click()
    last_name_input.clear()
    last_name_input.send_keys(s_name)

    post_code_input.click()
    post_code_input.clear()
    post_code_input.send_keys(p_code)

    add_button.click()

    alert = Alert(driver)

    print(alert)
    alert_text = alert.text
    print(alert_text)
    alert.accept()

    assert 'Customer added successfully' in alert_text

    if __name__ == "__main__":
       test_bank_add_customer()

