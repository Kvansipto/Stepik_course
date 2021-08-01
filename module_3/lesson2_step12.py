import unittest
#
#
# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()

from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"


class TestUnit(unittest.TestCase):

    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element_by_css_selector("[placeholder='Input your first name'").send_keys("Some answer")
        browser.find_element_by_css_selector("[placeholder='Input your last name'").send_keys("Some answer")
        browser.find_element_by_css_selector("[placeholder='Input your email'").send_keys("Some answer")
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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация не удалась")

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element_by_css_selector("[placeholder='Input your first name'").send_keys("Some answer")
        browser.find_element_by_css_selector("[placeholder='Input your last name'").send_keys("Some answer")
        browser.find_element_by_css_selector("[placeholder='Input your email'").send_keys("Some answer")
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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация не удалась")


if __name__ == "__main__":
    unittest.main()
