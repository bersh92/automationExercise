# Тест-кейс 2: Проверить наличие конкретной категории и кликнуть по ней

# Шаг 1: Открыть браузер
# Шаг 2: Зайти на сайт Automation Exercise
# Шаг 3: Найти раздел с категориями товаров
# Шаг 4: Просмотреть все категории в поисках конкретной, например, "Женская одежда"
# Шаг 5: Если эта категория есть, кликнуть по ней, чтобы перейти к товарам этой категории
# Шаг 6: Если этой категории нет, вывести сообщение, что такой категории не существует на сайте
# Шаг 7: Закрыть браузер

# Пример кода (предполагается, что студенты допишут его):
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("URL сайта")
# categories = driver.find_elements_by_css_selector("селектор списка категорий")
# category_found = False
# for category in categories:
#     if category.text == "Женская одежда":
#         category.click()
#         category_found = True
#         break
# if not category_found:
#     print("Категория 'Женская одежда' не найдена.")
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://automationexercise.com/')
categories = driver.find_elements(By.CSS_SELECTOR, 'div[class="panel-group category-products"] h4 a')

for category in categories:
    print(category.text)
if categories:  # Перевіряємо, чи знайдено хоча б одну категорію
    first_category = categories[0]  # Отримуємо перший елемент зі списку категорій
    first_category.click()  # Клікаємо на першу категорію
    print("Clicked on the first category")
else:
    print("No categories found")

driver.quit()