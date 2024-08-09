'''ТЭСТ-ШМЭСТ
для странички https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer
         "проверка авторизации существующего пользователя"
'''
# data test
'''Your_Name = Hermoine Granger'''
# Expected Result
''' существующий пользователь авторизован выполнен переход на страничку аккаунта'''

# импорты и всякие библиатечки
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
# лезем в хром
    driver = webdriver.Chrome()
# переходим по ссылчику
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
    driver.get(url)
    # замутим генератор
    yield driver

def test_user_permit(driver):
    driver.implicitly_wait(10)
# нашлось поле Your Name по ID
    Your_Name = driver.find_element(By.ID, 'userSelect')
# тыкнули в поле Your Name
    Your_Name.click()
# пишу существующего пользователя Hermoine Granger
    Your_Name.send_keys('Hermoine Granger')
# ещё раз тыкнули в поле Your Name
    Your_Name.click()
#кнопка входа
    Button_Login = driver.find_element(By.CLASS_NAME, 'btn.btn-default')
    Button_Login.click()

    driver.implicitly_wait(10)# дождались весь DOM
    # убедимся что переход на аккаунт пользователя выполнен
    account_log = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/strong')
    wait = WebDriverWait(driver,10)  #ВОТ И ДОЖДАЛИСЬ ЗАГРУЗКИ СТРАНИЦЫ И НУЖНОГО ЭЛЕМЕНТА
    message_accoun_log = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/strong")
''' ____________А ВОТ АЛЕРТ КАК НЕ РАБОТАЛ ТАК И НЕ РАБОТАЕТ :( _____________  !!!  '''

    alert = Alert(driver)
    print(alert)
    alert_text = alert.text
    print(alert_text)
    alert.accept()

 # Проверяем текст алерта
    assert 'фсё получилось юзер залогился' in alert_textse
if __name__ == "__main__":
    test_user_permit()