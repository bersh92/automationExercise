# Тест-кейс 1: Список текстов элементов в верхней части экрана

# Шаг 1: Открыть браузер.
# Шаг 2: Зайти на сайт Automation Exercise.
# Шаг 3: Найти элементы в верхней части экрана (кнопки навигации).
# Шаг 4: Создать список и добавить в него текст каждого найденного элемента.
# Шаг 5: Напечатать полученный список текстов элементов.
# Шаг 6: Закрыть браузер.

# Пример кода (для заполнения студентами):
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("URL сайта")
# navigation_buttons = driver.find_elements_by_css_selector("селектор элементов навигации")
# button_texts = [button.text for button in navigation_buttons]
# print(button_texts)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://automationexercise.com/')
navigation_buttons = driver.find_elements(By.CSS_SELECTOR, 'ul[class="nav navbar-nav"] li a')
list_navigation_buttons = []
for navigation_button in navigation_buttons:
    list_navigation_buttons.append(navigation_button.text)

print(list_navigation_buttons)

driver.quit()
