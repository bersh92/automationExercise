import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class StepHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def get_how(self, locator):
        if locator.startswith("//") or locator.startswith("(//"):
            how = By.XPATH
        else:
            how = By.CSS_SELECTOR
        return how

    def specified_element_is_present(self, locator, time=3):
        try:
            WebDriverWait(self.wd, time).until(
                EC.presence_of_element_located((self.get_how(locator), locator)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def click_on_element(self, locator, scrollInToView = False):
        WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element = WebDriverWait(self.wd, 10).until(
            EC.element_to_be_clickable((self.get_how(locator), locator))
        )
        if scrollInToView:
            self.wd.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        ActionChains(self.wd).move_to_element(element).pause(0.5).click().perform()

    def input_text(self, locator, text):
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element.click()
        element.clear()
        element.send_keys(text)

    def get_list_of_elements(self, locator):
        by = self.get_how(locator)
        WebDriverWait(self.wd, 10).until(
            EC.presence_of_all_elements_located((self.get_how(locator), locator)))
        return self.wd.find_elements(by=by, value=locator)

    def get_element_text(self, locator, scrollInToView = False):
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        if scrollInToView:
            self.wd.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        return element.text

    def specified_element_is_not_present(self, locator, waitingTime=3):
        time.sleep(1)
        WebDriverWait(self.wd, waitingTime).until(
            EC.invisibility_of_element_located((self.get_how(locator), locator)))

    def wait_for_element(self, locator):
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        return element

    def jsXpathClick (self, locator):
        time.sleep(2)
        b = self.wd.find_element(By.XPATH, locator)
        self.wd.execute_script("arguments[0].click();", b)

    def select_dropdown_by_value(self, locator, value):
        dropdown = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        Select(dropdown).select_by_value(value)

    def select_dropdown_by_text(self, locator, text):
        dropdown = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        Select(dropdown).select_by_visible_text(text)

    def get_elements_texts(self, locator):
        WebDriverWait(self.wd, 10).until(
            EC.presence_of_all_elements_located((self.get_how(locator), locator)))
        elements = self.wd.find_elements(self.get_how(locator), locator)
        time.sleep(1)
        texts = []
        for element in elements:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            text = element.text.strip()
            texts.append(text)
        return texts

    def close_popup_if_present(self, popup_locator, timeout=1.2):
        """
        This method checks for popups inside known iframes and closes them if present.
        :param popup_locator: The CSS selector or XPATH of the popup's dismiss button within the iframes.
        :param timeout: The maximum time to wait for the popup to appear.
        """
        # List of known iframe IDs to check for popups
        known_iframe_ids = ["iframe[id*='aswift'][style*='visibility: visible']", 'iframe[id="ad_iframe"]']  # Add other iframe IDs as needed

        for iframe_id in known_iframe_ids:
            try:
                # Switch to the iframe by ID
                WebDriverWait(self.wd, timeout).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, iframe_id)))

                # Wait for the popup dismiss button to appear inside the iframe
                dismiss_button = WebDriverWait(self.wd, timeout).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, popup_locator))
                )
                # Click the dismiss button to close the popup
                dismiss_button.click()
                print(f"Popup dismissed in iframe {iframe_id}.")
            except TimeoutException:
                # If the dismiss button is not found within the timeout, move on to the next iframe
                print(f"No popup was present in iframe {iframe_id}.")
            finally:
                # Always switch back to the default content before trying the next iframe
                self.wd.switch_to.default_content()