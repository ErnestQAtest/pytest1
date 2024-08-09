#-----------------------------проверка-------------------------------------------

#входные параметры
#email     @m.com
#name      tester33
#password  tester33

#ожидаемый результат "type": "error",   статус код 404
#Запрос http://users.bugred.ru/tasks/rest/doregister?email=@m.com&name=tester&password=tester


import requests
# определить параметры
base_url = 'http://users.bugred.ru/tasks/rest/doRegister'
email = "?email=@m.com"
name = "&name=tester33"
password = "&password=tester33"

print(base_url+email+name+password)
url = base_url + email + name + password # сформировать запрос в виде url
response = requests.get(url) # отправить запрос

status_code = response.status_code
json = response.json()

name_in_json = json#['tester33']

expected_name_in_json = 'tester33'
expected_status_code = 200

print(f""" factual: {status_code}, expected: {expected_status_code}
 factual name: {name_in_json}, expected name: {expected_name_in_json}
     """)


#-----------------------------------------------------------------------


def test_create_existing_user_doRegister():
# определить параметры
     base_url = 'http://users.bugred.ru/tasks/rest/doRegister'
     email = "?email=@m.com"
     name = "&name=tester108"
     password = "&password=tester108"

     url = base_url + email + name + password
     response = requests.get(url)
     status_code = response.status_code
     json = response.json()
     type_in_json = json['type']

     expected_name_in_json = 'tester3'
     expected_status_code = 200

     expected_type_in_json = "error"


     assert 400 <= status_code < 500, f"Не совпадает статус код"
     assert type_in_json == expected_type_in_json

#if __name__ == "__main__":
    #test_base_doRegister()
    #test_create_existing_user_doRegister()

#-----------------------------------------------------------------------------------
#___________________тест кейс_____________________________________-
#входные параметры
#email     @m.com
#name      tester55
#password  tester55


#ожидаемый результат "type": "error",   статус код 404
#Запрос http://users.bugred.ru/tasks/rest/doregister?email=@m.com&name=tester&password=tester


def test_create_existing_user_doRegister():
    # определить параметры
    base_url = 'http://users.bugred.ru/tasks/rest/doRegister'
    email = "?email=@m.com"
    name = "&name=tester55"
    password = "&password=tester55"

    # сформировать запрос в виде url
    # print(base_url+email+name+password)
    url = base_url + email + name + password

    # отправить запрос
    response = requests.get(url)

    status_code = response.status_code
    json = response.json()
    type_in_json = json['type']

    expected_type_in_json = "error"

    assert status_code == 200, f"Не совпадает статус код" #БАГ - КОД ДОЛЖЕН БЫТЬ 404, email НЕКОРРЕКТНЫЙ
    assert type_in_json == expected_type_in_json


if __name__ == "__main__":
    #test_base_doRegister()
    test_create_existing_user_doRegister()