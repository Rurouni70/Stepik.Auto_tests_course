# Задание: ждем нужный текст на странице - работа с явными ожиданиями

import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))  # Дождаться, когда цена дома уменьшится до 10000 RUR
    browser.find_element_by_id('book').click()  # Нажать на кнопку "Забронировать"



    num = browser.find_element_by_id("input_value").text
    browser.find_element_by_tag_name("input").send_keys(calc(int(num)))   # Считаем значение и записываем в форму ввода
    browser.find_element_by_id("solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()