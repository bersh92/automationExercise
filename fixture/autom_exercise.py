import os

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fixture.step import StepHelper


class AutomExercise:
    test_cases_button = "//div[@class='item active']//a[@class='test_cases_list']"
    automation_experience_text = "(//div[@class='col-sm-6']/h1)[1]"
    login_signup_button = "a[href='/login'] i"
    new_user_sign_up_text = "div[class='signup-form'] h2"
    login_to_your_account_text = "div[class='login-form'] h2"
    sign_up_name_field = "input[data-qa='signup-name']"
    sign_up_email_field = "input[data-qa='signup-email']"
    enter_login_email_address = "input[data-qa='login-email']"
    enter_login_password = "input[data-qa='login-password']"
    sign_up_button = "button[data-qa='signup-button']"
    login_button = "button[data-qa='login-button']"
    enter_account_information_text = "//b[text()='Enter Account Information']"
    title_mr_selector = "input[name='title'][value='Mr']"
    title_mrs_selector = "input[name='title'][value='Mrs']"
    name_input_selector = "input[data-qa='name']"
    email_input_selector = "input[data-qa='email']"
    password_input_selector = "input[data-qa='password']"
    day_selector = "#days"
    month_selector = "#months"
    year_selector = "#years"
    newsletter_checkbox_selector = "input[name='newsletter']"
    special_offers_checkbox_selector = "input[name='optin']"
    first_name_input_selector = "input[data-qa='first_name']"
    last_name_input_selector = "input[data-qa='last_name']"
    company_input_selector = "input[data-qa='company']"
    address_input_selector = "input[data-qa='address']"
    address2_input_selector = "input[data-qa='address2']"
    country_selector = "#country"
    state_input_selector = "input[data-qa='state']"
    city_input_selector = "input[data-qa='city']"
    zipcode_input_selector = "input[data-qa='zipcode']"
    mobile_number_input_selector = "input[data-qa='mobile_number']"
    create_account_button_selector = "button[data-qa='create-account']"
    account_created_text_selector = "h2[data-qa='account-created'] b"
    continue_button_selector = "a[data-qa='continue-button']"
    logged_in_text_selector = "//i[@class='fa fa-user']/parent::a"
    delete_account_button_selector = "//a[contains(text(), 'Delete Account')]"
    account_deleted_text = "h2[data-qa='account-deleted'] b"
    your_email_or_password_is_incorrect_text = "div[class='login-form'] p"
    log_out_button = "//a[contains(text(), 'Logout')]"
    email_address_already_exist_text = "div[class='signup-form'] p"
    contact_us_button = "a[href='/contact_us'] i"
    get_in_touch_text = "div[class='contact-form'] h2"
    contact_us_get_in_touch_name_field = "input[data-qa='name']"
    contact_us_get_in_touch_email_field = "input[data-qa='email']"
    contact_us_get_in_touch_subject_field = "input[data-qa='subject']"
    contact_us_get_in_touch_message_field = "textarea[data-qa='message']"
    upload_file_selector = "input[name='upload_file']"
    submit_button = 'input[data-qa="submit-button"]'
    success_your_details_have_been_submitted_successfully_text = "div[class='status alert alert-success']"
    home_button = 'a[class="btn btn-success"] span'
    test_cases_text = 'div[class="col-sm-9 col-sm-offset-1"] b'
    products_button = 'a[href="/products"] i'
    all_products_text = 'h2[class="title text-center"]'
    products_list = 'div[class="productinfo text-center"] p'
    view_product_first = 'a[href="/product_details/1"]'
    product_name_text = 'div[class="product-information"] h2'
    product_category_text = '(//div[@class="product-information"]/p) [1]'
    product_price_text = 'div[class="product-information"] span span'
    product_availability_text = '(//div[@class="product-information"]/p) [2]'
    product_condition_text = '(//div[@class="product-information"]/p) [3]'
    product_brand_text = '(//div[@class="product-information"]/p) [4]'
    pop_up = "div[id='dismiss-button']"

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd

    def get_enter_account_information_text(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.enter_account_information_text)

    def click_on_test_cases_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.test_cases_button)

    def set_sign_up_name_and_email(self, name, email):
        self.step.close_popup_if_present(self.pop_up)
        self.step.input_text(self.sign_up_name_field, name)
        self.step.input_text(self.sign_up_email_field, email)

    def enter_correct_email_and_password(self, email, password):
        self.step.close_popup_if_present(self.pop_up)
        self.step.input_text(self.enter_login_email_address, email)
        self.step.input_text(self.enter_login_password, password)

    def verify_that_user_is_navigated_to_login_page(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.specified_element_is_present(self.enter_login_email_address)
        self.step.specified_element_is_present(self.enter_login_password)

    def enter_incorrect_email_and_password(self, email, password):
        self.step.close_popup_if_present(self.pop_up)
        self.step.input_text(self.enter_login_email_address, email)
        self.step.input_text(self.enter_login_password, password)

    def click_sign_up_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.sign_up_button)

    def openUrl(self, url):
        self.wd.get(url)

    def get_automation_experience_text(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.automation_experience_text)

    def get_new_user_sign_up_text(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.new_user_sign_up_text)

    def get_login_to_your_account_text(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.login_to_your_account_text)

    def click_login_signup_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.login_signup_button)

    def click_login_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.login_button)

    def fill_account_information(self, title, name, password, dob):
        self.step.close_popup_if_present(self.pop_up)
        title_locator = self.title_mr_selector if title == 'Mr' else self.title_mrs_selector
        self.step.click_on_element(title_locator)
        self.step.input_text(self.name_input_selector, name)
        self.step.input_text(self.password_input_selector, password)
        day, month, year = dob.split('/')
        self.step.select_dropdown_by_value(self.day_selector, day)
        self.step.select_dropdown_by_value(self.month_selector, month)
        self.step.select_dropdown_by_value(self.year_selector, year)

    def select_newsletter_and_special_offers(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.newsletter_checkbox_selector)
        self.step.click_on_element(self.special_offers_checkbox_selector)

    def fill_address_information(self, first_name, last_name, company, address, address2, country, state, city, zipcode,
                                 mobile_number):
        self.step.close_popup_if_present(self.pop_up)
        self.step.input_text(self.first_name_input_selector, first_name)
        self.step.input_text(self.last_name_input_selector, last_name)
        self.step.input_text(self.company_input_selector, company)
        self.step.input_text(self.address_input_selector, address)
        self.step.input_text(self.address2_input_selector, address2)
        self.step.select_dropdown_by_text(self.country_selector, country)
        self.step.input_text(self.state_input_selector, state)
        self.step.input_text(self.city_input_selector, city)
        self.step.input_text(self.zipcode_input_selector, zipcode)
        self.step.input_text(self.mobile_number_input_selector, mobile_number)

    def create_account(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.create_account_button_selector)

    def click_logout(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.log_out_button)

    def verify_account_created(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.account_created_text_selector)

    def click_continue_after_account_creation(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.continue_button_selector)

    def verify_logged_in_user_display(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.logged_in_text_selector)

    def delete_account(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.delete_account_button_selector)

    def verify_account_deleted(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.account_deleted_text)

    def get_your_email_or_password_is_incorrect(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.your_email_or_password_is_incorrect_text)

    def get_email_address_already_exist(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.email_address_already_exist_text)

    def click_on_contact_us_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.contact_us_button)

    def get_get_in_touch_text(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.get_in_touch_text)

    def set_contact_us_get_in_touch_name_email_subject_and_message(self, name, email, subject, message):
        self.step.close_popup_if_present(self.pop_up)
        self.step.input_text(self.contact_us_get_in_touch_name_field, name)
        self.step.input_text(self.contact_us_get_in_touch_email_field, email)
        self.step.input_text(self.contact_us_get_in_touch_subject_field, subject)
        self.step.input_text(self.contact_us_get_in_touch_message_field, message)

    def upload_the_file(self):
        self.step.close_popup_if_present(self.pop_up)
        file_input = self.wd.find_element(By.CSS_SELECTOR, self.upload_file_selector)
        root_directory = os.path.dirname(os.path.dirname(__file__))  # Navigate up to the root from 'test'
        file_path = os.path.join(root_directory, "file_to_upload.txt")
        file_input.send_keys(file_path)

    def click_submit_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.submit_button)

    def confirm_upload(self):
        self.step.close_popup_if_present(self.pop_up)
        timeout = 10
        try:
            WebDriverWait(self.wd, timeout).until(EC.alert_is_present())
            alert = self.wd.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("No alert was present after {} seconds".format(timeout))

    def get_success_your_details_have_been_submitted_successfully_text(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.success_your_details_have_been_submitted_successfully_text)

    def click_home_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.home_button)

    def verify_that_landed_to_home_page_successfully(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.specified_element_is_present(self.automation_experience_text)

    def verify_user_is_navigated_to_test_cases_page_successfully(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.specified_element_is_present(self.test_cases_text)

    def click_on_products_button(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.products_button)

    def verify_user_is_navigated_to_all_products_page_successfully(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.specified_element_is_present(self.all_products_text)

    def get_products_names(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_elements_texts(self.products_list)

    def click_on_view_product_of_first_product(self):
        self.step.close_popup_if_present(self.pop_up)
        self.step.click_on_element(self.view_product_first, True)

    def get_product_name(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.product_name_text)

    def get_product_category(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.product_category_text)

    def get_product_price(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.product_price_text)

    def get_product_availability(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.product_availability_text)

    def get_product_condition(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.product_condition_text)

    def get_product_brand(self):
        self.step.close_popup_if_present(self.pop_up)
        return self.step.get_element_text(self.product_brand_text)
