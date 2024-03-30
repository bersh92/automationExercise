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

list_of_products = []
number_of_products_more_than_600 = 0

for i in products:
    name = i.find_element(By.CSS_SELECTOR, "p").text
    price = i.find_element(By.CSS_SELECTOR, "h2").text
    if len(price) > 3:
        price_formatted = price.split(' ')
        actual_price = int(price_formatted[1])
        if actual_price > 600:
            number_of_products_more_than_600 = number_of_products_more_than_600 + 1
    list_of_products.append(name)
    list_of_products.append(price)
    print(f"Product: {name}, Price: {price}")

print(list_of_products)
print('PRODUCTS MORE THAN 600',number_of_products_more_than_600)

driver.quit()
