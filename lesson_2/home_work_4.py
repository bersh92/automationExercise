# Тест-кейс 2: Проверка наличия элемента с названием, начинающимся на "LoggedInS", и клик по кнопке "Logout"

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
# if not logged_in_element_found:
#     print("Пользователь не залогинен.")
# driver.quit()
