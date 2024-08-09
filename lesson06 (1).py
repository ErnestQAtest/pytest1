#---------------------------#
# //span - ищет все элементы span
# //span[text()='подробно']  -   ищет элемент span с текстом "подробно"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
#@pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     url = "http://shop.bugred.ru/shop/item/21"
#     driver.get(url)
#     yield driver


@pytest.mark.parametrize('input_count, expected_count', [('2', '2'), ('-1', '1'), ('200', '100'), ('', '0'), ('!<{№', '0')])
def test_card_item( input_count, expected_count):
    try:
        driver = webdriver.Chrome()
        url = "http://shop.bugred.ru/shop/item/21"
        driver.get(url)
        driver.implicitly_wait(10) # ожидаем пока DOM полностью загрузиться

        count_input_field = driver.find_element(By.ID, 'exampleCount')
        count_input_field.click()
        count_input_field.send_keys(input_count)

        button_add_to_cart = driver.find_element(By.CLASS_NAME, 'btn.btn-primary') #кнопка  добавить в корзину
        button_add_to_cart.click()

        # определяем фактические результат
        count_in_cart = driver.find_element(By.CSS_SELECTOR, ".float-right .nav-link ")
        actual_result = count_in_cart.text
        #time.sleep(5)



    except Exception as err:
        print(err)

    #проверка
    assert actual_result == str(expected_count)
def test_card_clear():
    driver = webdriver.Chrome()
    url = "http://shop.bugred.ru/shop/item/21"
    driver.get(url)
    driver.implicitly_wait(10)  # ожидаем пока DOM полностью загрузиться



    count_input_field = driver.find_element(By.ID, 'exampleCount')
    count_input_field.click()
    count_input_field.send_keys(1)

    button_add_to_cart = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')  # кнопка  добавить в корзину
    button_add_to_cart.click()



    # переход в карзину
    url = 'http://shop.bugred.ru/shop/cart/index'
    driver.get(url)
    driver.implicitly_wait(10) # ожидаем пока DOM полностью загрузиться

    btn_delete = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(5) > a')
    btn_delete.click()

    # Ждем, пока элемент появится на странице
    wait = WebDriverWait(driver, 10)
    message_empty_cart = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Ваша корзина пуста!']")))
    #message_empty_cart = driver.find_element(By.XPATH, "//p[text()='Ваша корзина пуста!']")

    assert message_empty_cart.text == 'Ваша корзина пуста!'
if __name__ == "__main__":
    test_card_item()