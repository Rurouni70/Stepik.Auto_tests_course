# Задание: загрузка файла

import time
import os
from selenium import webdriver

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input_forms = browser.find_elements_by_class_name("form-control")
    for form in input_forms:
        form.send_keys("Test")

    download_element = browser.find_element_by_name('file')
    download_element.send_keys(file_path)

    browser.find_element_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()