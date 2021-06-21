import math
import time

from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    button.click()
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Anton")
    input1 = browser.find_element_by_name("last_name")
    input1.send_keys("Zhdanok")
    input1 = browser.find_element_by_class_name("city")
    input1.send_keys("Novosibirsk")
    input1 = browser.find_element_by_id("country")
    input1.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
