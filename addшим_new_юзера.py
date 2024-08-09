'''ТЭСТ-ШМЭСТ
для странички https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust
         "проверка добавления нового пользователя"
'''
# Input test data
''' 1. First Name = Erick
    2. Last Name = Shiva
    3. Post Code = 12345   '''
# Expected Result
''' Добавится новый пользователь - Erick Shiva   '''

# импорты и всякие библиатечки
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# чтобы получить систему в известном состоянии перед запуском теста нафикстурим
@pytest.fixture()
def driver():
# лезем в хром
    driver = webdriver.Chrome()
# переходим по ссылчику
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"
    driver.get(url)
    # замутим генератор
    yield driver
def test_check_user(driver):
# какаето неявная ожидалка странички
    driver.implicitly_wait(10)
# нашлось поле First Name по хпасу
    First_Name = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')
# тыкнули в это поле
    First_Name.click()
# написали в нём Erick
    First_Name.send_keys('Erick')
# нашлось поле Last Name по хпасу
    Last_Name = driver.find_element(By.XPATH,'//input[@placeholder="Last Name"]')
# фокус на поле
    Last_Name.click()
# написали в нём Shiva
    Last_Name.send_keys('Shiva')
# нашлось поле Post Code по хпасу
    Post_Code = driver.find_element(By.XPATH,'//input[@placeholder="Post Code"]')
# тык в него
    Post_Code.click()
# ввели данные 12345
    Post_Code.send_keys('12345')
# нашлась кнопочка "добавить пользователя"
    button_Add_Customer = driver.find_element(By.CLASS_NAME, 'btn.btn-default')
    button_Add_Customer.click()
# жамкнули кнопочку Add Customer

# проверка с алертам что тест кликером прошёлся по всем полям и создался юзер
    alert = Alert(driver)
    print(alert)
    alert_text = alert.text
    print(alert_text)
    alert.accept()

# Проверяем текст алерта
    assert 'фсё получилось юзер добавлен' in alert_text
if __name__ == "__main__":
    test_check_user()