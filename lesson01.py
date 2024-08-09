from authorization_module import *
import pytest
import requests


# def test_base_authorization():
#     test_data = ['username1', 'password1']
#     expected_result = 'Вход разрешен' # ожидаемый результат
#     actual_result = authenticate(test_data[0], test_data[1]) #Фактический результат authenticate(test_data*)
#     assert actual_result == expected_result, f" {expected_result} != {actual_result} "
#
# def test_with_incorrect_password_authorization():
#     test_data = ['username1', 'pppppp']
#     expected_result = 'Вход не разрешен'  # ожидаемый результат
#     actual_result = authenticate(test_data[0], test_data[1])  # Фактический результат authenticate(test_data*)
#     assert actual_result == expected_result, f" {expected_result} != {actual_result} "
#
#
# def test_with_stranger_password_authorization():
#     test_data = ['username1', 'password2'] # password2 пароль от другого пользователь
#     expected_result = 'Вход не разрешен'  # ожидаемый результат
#     actual_result = authenticate(test_data[0], test_data[1])  # Фактический результат authenticate(test_data*)
#     assert actual_result == expected_result, f" {expected_result} != {actual_result} "


'''





# ----------------------------Тестирование запросов--------------------------------- #

'''
# Test case:
#
# данные:
#     * указываем запрос https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla
#     * параметры:
#         * api_key = jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla
#         * без даты и без дополнительных параметров
#
# Ожидаемый результат:
#     * получение json-файла и статус код равен 200
'''
def test_base_request_with_api_key():
    base_url = 'https://api.nasa.gov/planetary/apod?'
    api_key = 'api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla'

    url_request = base_url + api_key

    expected_status_code = 200
    response = requests.get(url_request) # requests.get(url_request) - получение ответа от сервера
    actual_status_code = response.status_code

    assert actual_status_code == expected_status_code

    expected_content = True # строка не пустая
    actual_content = response.json()#
    assert bool(actual_content) == expected_content





'''
# Test case:
#
# данные:
#     * указываем запрос https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla
#     * параметры:
#         * api_key = jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla
#         * дата : 2020-09-03  # YYYY-MM-DD
#
# Ожидаемый результат:
#     * получение json-файла и статус код равен 200

def test_base_request_with_api_key_and_date():
    base_url = 'https://api.nasa.gov/planetary/apod?'
    api_key = 'api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla'
    date = '&date=2020-09-03'
    url_request = base_url + api_key + date

    expected_status_code = 200
    response = requests.get(url_request) # requests.get(url_request) - получение ответа от сервера

    actual_status_code = response.status_code
    assert actual_status_code == expected_status_code

    expected_content = True # строка не пустая
    actual_content = response.json()#
    assert bool(actual_content) == expected_content

    # get_img = response.json()['url'] - для получения изображения


def test_base_request_with_content():
    base_url = 'https://api.nasa.gov/planetary/apod?'
    api_key = 'api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla'
    date = '&date=2024-04-23'
    url_request = base_url + api_key + date

    expected_status_code = 200
    response = requests.get(url_request)
    actual_status_code = response.status_code
    assert actual_status_code == expected_status_code

    actual_content = response.json()
    assert bool(actual_content) == True








# def test_status_code_200():
#     date = "2023-10-10"
#     url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
#     response = requests.request(url=url, method='GET')
#     result = response.status_code
#    assert  200 <= result < 400


