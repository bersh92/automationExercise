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

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd

    def get_enter_account_information_text(self):
        return self.step.get_element_text(self.enter_account_information_text)

    def click_on_test_cases_button(self):
        self.step.click_on_element(self.test_cases_button)

    def set_sign_up_name_and_email(self, name, email):
        self.step.input_text(self.sign_up_name_field, name)
        self.step.input_text(self.sign_up_email_field, email)

    def enter_correct_email_and_password(self, email, password):
        self.step.input_text(self.enter_login_email_address, email)
        self.step.input_text(self.enter_login_password, password)

    def enter_incorrect_email_and_password(self, email, password):
        self.step.input_text(self.enter_login_email_address, email)
        self.step.input_text(self.enter_login_password, password)

    def click_sign_up_button(self):
        self.step.click_on_element(self.sign_up_button)

    def openUrl(self, url):
        self.wd.get(url)

    def get_automation_experience_text(self):
        return self.step.get_element_text(self.automation_experience_text)

    def get_new_user_sign_up_text(self):
        return self.step.get_element_text(self.new_user_sign_up_text)

    def get_login_to_your_account_text(self):
        return self.step.get_element_text(self.login_to_your_account_text)

    def click_login_signup_button(self):
        self.step.click_on_element(self.login_signup_button)

    def click_login_button(self):
        self.step.click_on_element(self.login_button)

    def fill_account_information(self, title, name, password, dob):
        title_locator = self.title_mr_selector if title == 'Mr' else self.title_mrs_selector
        self.step.click_on_element(title_locator)
        self.step.input_text(self.name_input_selector, name)
        self.step.input_text(self.password_input_selector, password)
        day, month, year = dob.split('/')
        self.step.select_dropdown_by_value(self.day_selector, day)
        self.step.select_dropdown_by_value(self.month_selector, month)
        self.step.select_dropdown_by_value(self.year_selector, year)

    def select_newsletter_and_special_offers(self):
        self.step.click_on_element(self.newsletter_checkbox_selector)
        self.step.click_on_element(self.special_offers_checkbox_selector)

    def fill_address_information(self, first_name, last_name, company, address, address2, country, state, city, zipcode,
                                 mobile_number):
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
        self.step.click_on_element(self.create_account_button_selector)

    def click_logout(self):
        self.step.click_on_element(self.log_out_button)

    def verify_account_created(self):
        return self.step.get_element_text(self.account_created_text_selector)

    def click_continue_after_account_creation(self):
        self.step.click_on_element(self.continue_button_selector)

    def verify_logged_in_user_display(self):
        return self.step.get_element_text(self.logged_in_text_selector)

    def delete_account(self):
        self.step.click_on_element(self.delete_account_button_selector)

    def verify_account_deleted(self):
        return self.step.get_element_text(self.account_deleted_text)

    def verifi_your_email_or_password_is_incorrect(self):
        return self.step.get_element_text(self.your_email_or_password_is_incorrect_text)