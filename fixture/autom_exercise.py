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
    pop_up = "div[id='dismiss-button'] div"
    search_product = 'input[type="text"]'
    search_button = 'button[type="button"] i'
    list_search_products = 'div[class="productinfo text-center"] p'
    subscription_text = 'div[class="single-widget"] h2'
    subscription_input_email_address = 'input[type="email"]'
    subscription_arrow_button = 'button[type="submit"] i'
    success_message_subscribed_text = 'div[class="alert-success alert"]'
    cart_button = 'a[href="/view_cart"] i'
    add_to_cart_first_product = '(//div[@class="productinfo text-center"]//a//i) [1]'
    continue_shopping_button = 'button[class="btn btn-success close-modal btn-block"]'
    add_to_cart_second_product = '(//div[@class="productinfo text-center"]//a//i) [2]'
    view_cart_button = 'a[href="/view_cart"] u'
    list_products_are_added_to_cart_text = '//div[@class="table-responsive cart_info"]//h4//a'
    view_product_third = 'a[href="/product_details/3"]'
    inp_quantity = 'input[id="quantity"]'
    add_to_cart_button = 'button[type="button"] i'
    add_to_cart_third_product = '(//div[@class="productinfo text-center"]//a//i) [3]'
    proceed_to_checkout = 'a[class="btn btn-default check_out"]'
    register_login_button = 'div[class="modal-body"] u'
    comment_text_area = 'textarea[class="form-control"]'
    place_order_button = 'a[href="/payment"]'
    name_card_input_selector = 'input[name="name_on_card"]'
    number_card_input_selector = 'input[name="card_number"]'
    cvc_card_input_selector = 'input[name="cvc"]'
    expiration_date_card_month_input_selector = 'input[name="expiry_month"]'
    expiration_date_card_year_input_selector = 'input[name="expiry_year"]'
    pay_and_confirm_order_button = 'button[data-qa="pay-button"]'
    success_message_your_order_has_been_placed_successfully_text = 'div[id="success_message"] div'

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

    def verify_that_user_is_navigated_to_login_page(self):
        self.step.specified_element_is_present(self.enter_login_email_address)
        self.step.specified_element_is_present(self.enter_login_password)

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
        if title == 'Mr':
            title_locator = self.title_mr_selector
        else:
            title_locator = self.title_mrs_selector
        self.step.click_on_element(title_locator)
        self.step.input_text(self.name_input_selector, name)
        self.step.input_text(self.password_input_selector, password)
        split_string = dob.split('/')
        day = split_string[0]
        month = split_string[1]
        year = split_string[2]
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

    def get_your_email_or_password_is_incorrect(self):
        return self.step.get_element_text(self.your_email_or_password_is_incorrect_text)

    def get_email_address_already_exist(self):
        return self.step.get_element_text(self.email_address_already_exist_text)

    def click_on_contact_us_button(self):
        self.step.click_on_element(self.contact_us_button)

    def get_get_in_touch_text(self):
        return self.step.get_element_text(self.get_in_touch_text)

    def set_contact_us_get_in_touch_name_email_subject_and_message(self, name, email, subject, message):
        self.step.input_text(self.contact_us_get_in_touch_name_field, name)
        self.step.input_text(self.contact_us_get_in_touch_email_field, email)
        self.step.input_text(self.contact_us_get_in_touch_subject_field, subject)
        self.step.input_text(self.contact_us_get_in_touch_message_field, message)

    def upload_the_file(self):
        file_input = self.wd.find_element(By.CSS_SELECTOR, self.upload_file_selector)
        root_directory = os.path.dirname(os.path.dirname(__file__))  # Navigate up to the root from 'test'
        file_path = os.path.join(root_directory, "file_to_upload.txt")
        file_input.send_keys(file_path)

    def click_submit_button(self):
        self.step.click_on_element(self.submit_button)

    def confirm_upload(self):
        timeout = 10
        try:
            WebDriverWait(self.wd, timeout).until(EC.alert_is_present())
            alert = self.wd.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("No alert was present after {} seconds".format(timeout))

    def get_success_your_details_have_been_submitted_successfully_text(self):
        return self.step.get_element_text(self.success_your_details_have_been_submitted_successfully_text)

    def click_home_button(self):
        self.step.click_on_element(self.home_button)

    def verify_that_landed_to_home_page_successfully(self):
        self.step.specified_element_is_present(self.automation_experience_text)

    def verify_user_is_navigated_to_test_cases_page_successfully(self):
        self.step.specified_element_is_present(self.test_cases_text)

    def click_on_products_button(self):
        self.step.click_on_element(self.products_button)

    def verify_user_is_navigated_to_all_products_page_successfully(self):
        self.step.specified_element_is_present(self.all_products_text)

    def get_products_names(self):
        return self.step.get_elements_texts(self.products_list)

    def click_on_view_product_of_first_product(self):
        self.step.click_on_element(self.view_product_first, True)

    def get_product_name(self):
        return self.step.get_element_text(self.product_name_text)

    def get_product_category(self):
        return self.step.get_element_text(self.product_category_text)

    def get_product_price(self):
        return self.step.get_element_text(self.product_price_text)

    def get_product_availability(self):
        return self.step.get_element_text(self.product_availability_text)

    def get_product_condition(self):
        return self.step.get_element_text(self.product_condition_text)

    def get_product_brand(self):
        return self.step.get_element_text(self.product_brand_text)

    def enter_product_name_in_search_input(self, search):
        self.step.input_text(self.search_product, search)

    def click_search_button(self):
        self.step.click_on_element(self.search_button)

    def get_all_product_names_related_to_search_are_visible(self):
        return self.step.get_elements_texts(self.list_search_products)

    def get_subscription_text(self):
        return self.step.get_element_text(self.subscription_text)

    def enter_email_address_in_input(self, email):
        self.step.input_text(self.subscription_input_email_address, email)

    def click_arrow_button_subscription(self):
        self.step.click_on_element(self.subscription_arrow_button, True)

    def get_success_message_subscribed(self):
        return self.step.get_element_text(self.success_message_subscribed_text)

    def click_cart_button(self):
        self.step.click_on_element(self.cart_button)

    def click_add_to_cart_on_first_product(self):
        self.step.click_on_element(self.add_to_cart_first_product, True)

    def click_continue_shopping_button(self):
        self.step.click_on_element(self.continue_shopping_button)

    def click_add_to_cart_on_second_product(self):
        self.step.click_on_element(self.add_to_cart_second_product, True)

    def click_view_cart_button(self):
        self.step.click_on_element(self.view_cart_button)

    def get_names_products_are_added_to_cart(self):
        return self.step.get_elements_texts(self.list_products_are_added_to_cart_text)

    def get_product_data(self, product_id):
        title = self.step.get_element_text(f'tr[id="product-{product_id}"] h4')
        price = self.step.get_element_text(f'tr[id="product-{product_id}"] td[class="cart_price"] p')
        quantity = self.step.get_element_text(f'tr[id="product-{product_id}"] td[class="cart_quantity"] button')
        total_price = self.step.get_element_text(f'tr[id="product-{product_id}"]  td[class="cart_total"] p')
        product = {
            "title": title,
            "price": price,
            "quantity": quantity,
            "total_price": total_price
        }
        return product

    def click_on_view_product_of_third_product(self):
        self.step.click_on_element(self.view_product_third, True)

    def get_product_detail_is_opened(self):
        name_product = self.step.get_element_text('div[class="product-information"] h2')
        category = self.step.get_element_text('(//div[@class="product-information"]/p) [1]')
        price = self.step.get_element_text('div[class="product-information"] span span')
        brand = self.step.get_element_text('(//div[@class="product-information"]/p) [4]')
        product = {
            "name_product": name_product,
            "category": category,
            "price": price,
            "brand": brand
        }
        return product

    def input_quantity(self, quantity):
        self.step.input_text(self.inp_quantity, quantity)

    def click_add_to_cart_button(self):
        self.step.click_on_element(self.add_to_cart_button)

    def click_add_to_cart_on_third_product(self):
        self.step.click_on_element(self.add_to_cart_third_product, True)

    def click_proceed_to_checkout(self):
        self.step.click_on_element(self.proceed_to_checkout)

    def click_register_login_button(self):
        self.step.click_on_element(self.register_login_button)

    def get_details_delivery_address(self):
        first_and_last_name = self.step.get_element_text(
            '//ul[@class="address item box"]//li[@class="address_firstname address_lastname"]')
        address = self.step.get_element_text(
            '(//ul[@class="address item box"]//li[@class="address_address1 address_address2"]) [2]')
        city = self.step.get_element_text(
            '//ul[@class="address item box"]//li[@class="address_city address_state_name address_postcode"]')
        country = self.step.get_element_text('//ul[@class="address item box"]//li[@class="address_country_name"]')
        phone = self.step.get_element_text('//ul[@class="address item box"]//li[@class="address_phone"]')
        delivery_address = {
            "first_and_last_name": first_and_last_name,
            "address": address,
            "city": city,
            "country": country,
            "phone": phone
        }
        return delivery_address

    def get_details_billing_address(self):
        first_and_last_name = self.step.get_element_text(
            '//ul[@class="address alternate_item box"]//li[@class="address_firstname address_lastname"]')
        address = self.step.get_element_text(
            '(//ul[@class="address alternate_item box"]//li[@class="address_address1 address_address2"]) [2]')
        city = self.step.get_element_text(
            '//ul[@class="address alternate_item box"]//li[@class="address_city address_state_name address_postcode"]')
        country = self.step.get_element_text(
            '//ul[@class="address alternate_item box"]//li[@class="address_country_name"]')
        phone = self.step.get_element_text('//ul[@class="address alternate_item box"]//li[@class="address_phone"]')
        billing_address = {
            "first_and_last_name": first_and_last_name,
            "address": address,
            "city": city,
            "country": country,
            "phone": phone
        }
        return billing_address

    def input_description_in_comment_text_area(self, text):
        self.step.input_text(self.comment_text_area, text)

    def click_place_order_button(self):
        self.step.click_on_element(self.place_order_button, True)

    def fill_payment_details(self, name, number, cvc, month, year):
        self.step.input_text(self.name_card_input_selector, name)
        self.step.input_text(self.number_card_input_selector, number)
        self.step.input_text(self.cvc_card_input_selector, cvc)
        self.step.input_text(self.expiration_date_card_month_input_selector, month)
        self.step.input_text(self.expiration_date_card_year_input_selector, year)

    def click_pay_and_confirm_order_button(self):
        self.step.click_on_element(self.pay_and_confirm_order_button)

    def get_success_message_your_order_has_been_placed_successfully(self):
        return self.step.get_element_text(self.success_message_your_order_has_been_placed_successfully_text)