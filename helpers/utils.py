import os
import shutil
import random
import string

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
