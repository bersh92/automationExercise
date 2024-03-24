import os
import shutil
import random
import string
import requests

class Utils:

    def __init__(self, app):
        self.app = app
        self.step = self.app.step
        self.wd = self.app.wd

    BASEDIR = os.path.join(os.getcwd(), "screenshots/")

    def generate_random_email(domain='example.com', length=15):
        characters = string.ascii_letters + string.digits
        local_part = ''.join(random.choice(characters) for i in range(length))
        return f"{local_part}@{domain}"

    def takeScreenshot(self):
        shutil.rmtree(self.BASEDIR)
        os.makedirs(self.BASEDIR)
        self.wd.save_screenshot(self.BASEDIR + "test.png")

    def deleteAllScreenshots(self):
        shutil.rmtree(self.BASEDIR)
        os.makedirs(self.BASEDIR)

    def getPathToScreenshot(self):
        return self.BASEDIR + "test.png"

    def create_account_with_defaults(email, password):
        url = "https://automationexercise.com/api/createAccount"
        payload = {
            "name": "Default Name",
            "email": email,
            "password": password,
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "January",
            "birth_year": "1990",
            "firstname": "Default",
            "lastname": "User",
            "company": "Default Company",
            "address1": "123 Default St",
            "address2": "Suite 100",
            "country": "United States",
            "zipcode": "90001",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "1234567890"
        }
        response = requests.post(url, data=payload)

        if response.status_code == 201 or response.status_code == 200:
            print("\n!!! User created successfully !!!")
        else:
            print("\nFailed to create user. Status Code:", response.status_code)
            print("\nResponse:", response.text)

