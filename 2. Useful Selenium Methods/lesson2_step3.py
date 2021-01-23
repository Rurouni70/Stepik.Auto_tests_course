# Задание: работа с выпадающим списком

from selenium.webdriver.support.ui import Select  # Работа с выпадающим списком
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id("num1").text  # Вытаскиваем первое значение
    number2 = browser.find_element_by_id("num2").text  # Вытаскиваем второе значение
    summ = int(number1) + int(number2)

    select = Select(browser.find_element_by_tag_name("select"))  # Обьект для работы с выпадающим списком
    select.select_by_value(str(summ))  # ищем элемент со значением summ

    browser.find_elements_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
