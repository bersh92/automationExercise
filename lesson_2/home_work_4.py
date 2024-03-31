# Тест-кейс 2: Проверка наличия элемента с названием, начинающимся на "LoggedInS", и клик по кнопке "Logout"
import time

# Шаг 1: Открыть браузер.
# Шаг 2: Зайти на сайт Automation Exercise.
# Шаг 3: Найти элементы в верхней части экрана (кнопки навигации).
# Шаг 4: Итерировать по списку элементов, проверяя, начинается ли текст элемента на "LoggedInS".
# Шаг 5: Если элемент найден, кликнуть по кнопке "Logout".
#        Если элемент не найден, вывести сообщение о том, что пользователь не залогинен.
# Шаг 6: Закрыть браузер.

# Пример кода (для заполнения студентами):
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("URL сайта")
# navigation_elements = driver.find_elements_by_css_selector("селектор элементов навигации")
# logged_in_element_found = False
# for element in navigation_elements:
#     if element.text.startswith("LoggedInS"):
#         logout_button = driver.find_element_by_css_selector("селектор кнопки Logout")
#         logout_button.click()
#         logged_in_element_found = True
#         break
# if logged_in_element_found == False:
#     print("Пользователь не залогинен.")
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://automationexercise.com/')
signup_login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
signup_login.click()
first_element = driver.find_element(By.CSS_SELECTOR, 'form[action="/login"] input[type="email"]')
email = first_element.send_keys("email@jhf.com")
second_element = driver.find_element(By.CSS_SELECTOR, 'form[action="/login"] input[type="password"]')
password = second_element.send_keys('password')
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]')
login_button.click()

navigation_buttons = driver.find_elements(By.CSS_SELECTOR, 'ul[class="nav navbar-nav"] li a')

logout_button_value = "not found"

for navigation_button in navigation_buttons:
    print(navigation_button.text)
    if navigation_button.text.startswith("Logged in as"):
        logout_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/logout"]')
        logout_button.click()
        print("Logout found and clicked")
        logout_button_value = "found"
        break

if logout_button_value == "not found":
    print('Logout_not_found')

driver.quit()
