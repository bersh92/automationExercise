# Steps:
# 1. Import the webdriver and By from selenium.
# 2. Initialize the WebDriver for Chrome.
# 3. Use the driver to navigate to the product page URL.
# 4. Locate all product elements using By and CSS_SELECTOR.
# 5. Iterate over each product element to find and print the name and price contained within.
# 6. Close the browser.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationexercise.com")  # Adjust this URL

products = driver.find_elements(By.CSS_SELECTOR, ".single-products .productinfo")
for product in products:
    name = product.find_element(By.CSS_SELECTOR, "p").text
    price = product.find_element(By.CSS_SELECTOR, "h2").text
    print(f"Product: {name}, Price: {price}")

driver.quit()
