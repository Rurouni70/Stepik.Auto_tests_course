# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  # выдёргиваем значение для формулы
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)  # отправляем посчитанное значение
    browser.find_element_by_id("robotCheckbox").click()  # отмечаемся в чекбоксе
    browser.find_element_by_css_selector("[for='robotsRule']").click()  # отмечаем нужный радиобаттон
    browser.find_element_by_class_name("btn.btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
