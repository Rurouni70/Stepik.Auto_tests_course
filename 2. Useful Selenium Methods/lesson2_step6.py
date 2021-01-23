# Задание на execute_script
import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    nums = browser.find_element_by_id("input_value").text
    value = str(calc(int(nums)))

    browser.execute_script("window.scrollBy(0, 120);")
    browser.find_element_by_id('answer').send_keys(value)
    browser.find_element_by_id("robotCheckbox").click()  # отмечаемся в чекбоксе
    browser.find_element_by_css_selector("[for='robotsRule']").click()  # отмечаем нужный радиобаттон
    button = browser.find_element_by_tag_name("button")

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
