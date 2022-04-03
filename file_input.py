from selenium import webdriver
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    fname = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
    fname.send_keys('name')

    lname = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)")
    lname.send_keys('last name')

    email = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)")
    email.send_keys('gdh@sklflsd.kjf')

    file = browser.find_element_by_id("file")
    file.send_keys(file_path)
    

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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()