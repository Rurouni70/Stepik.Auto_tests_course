# поиск элемента по тексту в ссылке

from selenium import webdriver
import time
import math

first_link = "http://suninjuly.github.io/find_link_text"
second_link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(first_link)

    search_link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    search_link.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city") # Если в названии класса есть пробел, то меняем
    # на точку
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
