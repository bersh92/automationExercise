# Steps:
# 1. Import the webdriver and By from selenium.
# 2. Initialize the WebDriver for Chrome.
# 3. Navigate to the subscription page URL.
# 4. Input a test email into the subscription form's input field using By and CSS_SELECTOR.
# 5. Click the submit button.
# 6. Check for a success message and print a confirmation based on its presence using By and CSS_SELECTOR.
# 7. Close the browser.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationexercise.com")  # Adjust URL to where the subscription form is located

email_field = driver.find_element(By.CSS_SELECTOR, "#susbscribe_email")
email_field.send_keys("test@example.com")

subscribe_button = driver.find_element(By.CSS_SELECTOR, "#subscribe")
subscribe_button.click()
time.sleep(3)
# Assume there's an element that shows up for a successful subscription
# Adjust the CSS selector to the actual success message on your webpage
success_message = driver.find_element(By.CSS_SELECTOR, 'div[class="alert-success alert"]')

if success_message.text == 'You have been successfully subscribed!':
    print("Subscription successful.")
else:
    print("Subscription failed or no confirmation received.")

driver.quit()
