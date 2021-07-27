from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Anton")
    browser.find_element_by_name("lastname").send_keys("Zhdanok")
    browser.find_element_by_name("email").send_keys("zhd@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    browser.find_element_by_name("file").send_keys(file_path)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
