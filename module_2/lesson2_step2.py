from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    select = Select(browser.find_element_by_tag_name("select"))

    select.select_by_visible_text(str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
