

# from selenium import webdriver
# from selenium.webdriver.common.by import By # для поиска элементов DOMе
#
# from time import sleep
# driver = webdriver.Chrome()
# url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0"
# driver.get(url)
# #sleep(1) # !!! ВРЕМЕННАЯ МЕРА
#
# # Поиск элемента на странице
# try:
#     title = driver.find_element(By.TAG_NAME, 'h1') # элемент дома
#     print('title Элемент был найден')
#     class_name_element = driver.find_elements(By.CLASS_NAME, 'mw-jump-link')
#     print('class_name_element Элемент был найден', len(class_name_element))
#     # img_tag_name = driver.find_element(By.TAG_NAME, 'img')
#     # print(img_tag_name.get_dom_attribute('src'))
#     # img_link = driver.find_element(By.LINK_TEXT, '//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/275px-Cat_poster_1.jpg')
#     text_link = driver.find_element(By.LINK_TEXT, 'лесной кошкой')
#     print('text_link Элемент был найден', text_link)
#     selector = driver.find_element(By.CSS_SELECTOR, '')
#
# except Exception as err:
#     print(err)
#
#
# # # try except example
# # try:
# #     print(56/0)
# #     print('Все успешно')
# # except Exception as error:
# #     print('ошибка: ', error )



from selenium import webdriver
from selenium.webdriver.common.by import By # для поиска элементов DOMе

from time import sleep
driver = webdriver.Chrome()
url = "file:///C:/Users/Anastasia/Desktop/Groups/QA_328/OAT/html/index.html"
driver.get(url)
#sleep(1) # !!! ВРЕМЕННАЯ МЕРА

# Поиск элемента на странице
try:
    el = driver.find_element(By.CSS_SELECTOR, ' div p a.class.abc') # элемент дома
    print('el Элемент был найден', el.text)


except Exception as err:
    print(err)