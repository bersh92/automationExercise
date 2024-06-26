# Тест-кейс 1: Вывести список всех брендов
from selenium.webdriver.chrome import webdriver

# Шаг 1: Открыть браузер
# Шаг 2: Зайти на сайт Automation Exercise
# Шаг 3: Найти раздел, где перечислены все бренды
# Шаг 4: Пройтись по списку брендов и собрать их названия
# Шаг 5: Вывести на экран список всех названий брендов
# Шаг 6: Закрыть браузер

# Пример кода (предполагается, что студенты допишут его):
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("URL сайта")
# brands = driver.find_elements_by_css_selector("селектор списка брендов")
# for brand in brands:
#     print(brand.text)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://automationexercise.com/')
brands = driver.find_elements(By.CSS_SELECTOR, 'div[class="brands-name"] a')

for brand in brands:
    print(brand.text)

driver.quit()