'''
тест-кейсы
https://docs.google.com/spreadsheets/d/10wpXrRAeRNpMA-zSKCziBfczvsjhBNkTcc9F4hiC55s/edit?usp=sharing
'''
'''
1. корзина пуста
2. открыта страница http://shop.bugred.ru/shop/item/21 
3. нажать на поле "Количество"
4. ввести кол-во 
5. нажать на кнопку "Добавить в корзину"
OP
в корзине  2 товара

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    url = "http://shop.bugred.ru/shop/item/21"
    driver.get(url)
    yield driver

@pytest.mark.parametrize('input_count, expected_count', [('2', '2'), ('-1', '1'), ('200', '100'), ('', '0'), ('!<{№', '0')])
def test_card_item(driver, input_count, expected_count):
    try:

        count_input_field = driver.find_element(By.ID, 'exampleCount')
        count_input_field.click()


        count_input_field.send_keys(input_count)
        button_add_to_cart = driver.find_element(By.CLASS_NAME, 'btn.btn-primary') #кнопка  добавить в корзину
        button_add_to_cart.click()

        # определяем фактические результат
        count_in_cart = driver.find_element(By.CSS_SELECTOR, ".float-right .nav-link ")
        actual_result = count_in_cart.text
        # time.sleep(5)



    except Exception as err:
        print(err)

    #проверка
    assert actual_result == str(expected_count)