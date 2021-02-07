import unittest
from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def get_link(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    tag1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    tag2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    tag3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    tags = [tag1, tag2, tag3]
    for tag in tags:
        tag.send_keys("Test")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text


class TestSelector(unittest.TestCase):
    def test_one(self):
        self.assertEqual(get_link(link1), "Congratulations! You have successfully registered!", "registration is failed")

    def test_two(self):
        self.assertEqual(get_link(link2), "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    unittest.main()
