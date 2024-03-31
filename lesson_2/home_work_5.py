# Тест-кейс: Прокликивание всех тест-кейсов в drop-down меню

# Шаг 1: Открыть браузер.
# Шаг 2: Зайти на сайт Automation Exercise.
# Шаг 3: Кликнуть на элемент или кнопку "Test Cases".
# Шаг 4: Получить список всех элементов тест-кейсов, доступных в drop-down меню.
# Шаг 5: Используя цикл For, пройти по всем тест-кейсам в списке.
# Шаг 6: Кликнуть на каждый тест-кейс, чтобы открыть его содержимое в drop-down меню.
# Шаг 7: Закрыть браузер.

# Пример кода (для заполнения студентами):
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# driver = webdriver.Chrome()
# driver.get("URL сайта")
# test_cases_button = driver.find_element(By.CSS_SELECTOR, "селектор кнопки 'Test Cases'")
# test_cases_button.click()

# test_cases_elements = driver.find_elements(By.CSS_SELECTOR, "селектор элементов в drop-down меню")
# for test_case in test_cases_elements:
#     ActionChains(driver).move_to_element(test_case).click().perform()
#     time.sleep(1)  # Пауза, чтобы дать странице время на обработку каждого клика

# driver.quit()
