# Задание: поиск сокровища с помощью get_attribute
import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    munber_in_treasure = browser.find_element_by_id("treasure").get_attribute("valuex")
    y = calc(munber_in_treasure)

    browser.find_element_by_id("answer").send_keys(y)  # отправляем посчитанное значение
    browser.find_element_by_id("robotCheckbox").click()  # отмечаемся в чекбоксе
    browser.find_element_by_id("robotsRule").click()  # отмечаем нужный радиобаттон
    browser.find_element_by_tag_name("button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
