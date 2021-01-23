# Задание: принимаем alert

import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    browser.switch_to.alert.accept()  # Переключаемся на Alert и принимаем его
    num = browser.find_element_by_id("input_value").text
    browser.find_element_by_tag_name("input").send_keys(calc(int(num)))   # Считаем значение и записываем в форму ввода
    browser.find_element_by_tag_name("button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()