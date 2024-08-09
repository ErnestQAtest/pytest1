import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import result

'''
test-case id 1
проверка - существование треугольника при условии a+b>c
data:
A = 3
B = 5
C = 4
expected result:
"Треугольник существует"
негативная проверка - существование треугольника при условии a+b<c
data:
A = 1
B = 2
C = 5
expected result:
"Треугольник не существует"
'''

driver = webdriver.Chrome()
url = "https://allcalc.ru/node/1050"
driver.get(url)
time.sleep(3)
@pytest.mark.parametrize("SIDE_A, SIDE_B, SIDE_C, expected_result",[('3','5','4','Треугольник существует'),('1','2','5','Тркугольник не существует')])
def test_id_1(SIDE_A, SIDE_B, SIDE_C, expected_result):
    try:
        SIDE_A = driver.find_element(By.ID, 'value1')
        SIDE_B = driver.find_element(By.ID,'value2')
        SIDE_C = driver.find_elements(By.ID,'value3')

        SIDE_A.click()
        SIDE_A.send_keys(SIDE_A)

        SIDE_B.click()
        SIDE_B.send_keys(SIDE_B)

        SIDE_C.click(SIDE_C)
        SIDE_C.send_keys(SIDE_C)

        cls_button = driver.find_elements(By.tagName("td")).click()
                                          # XPATH ("//*[@id="calc"]/table/tbody/tr[5]/td/input")).click()
    # полный игспассс - /html/body/div[4]/div/div[1]/div[2]/center[2]/form/table/tbody/tr[5]/td/input
        result = driver.find_element(By.ID,'triangle')
    except Exception as err:
        pytest.fail(f"фсё плохо:{err}")
    assert result.text == expected_result,'Результат не ожидаемый'
driver.quit()
