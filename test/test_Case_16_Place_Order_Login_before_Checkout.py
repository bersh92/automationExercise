from helpers.utils import Utils

email = Utils.generate_random_email()
password = "TestPassword"
first = {'title': 'Blue Top', 'price': 'Rs. 500', 'quantity': '1', 'total_price': 'Rs. 500'}
third = {'title': 'Sleeveless Dress', 'price': 'Rs. 1000', 'quantity': '1', 'total_price': 'Rs. 1000'}
delivery_address = {'first_and_last_name': 'Mr. FirstName LastName', 'address': 'Address', 'city': 'City State 12345',
                    'country': 'United States', 'phone': '1234567890'}
billing_address = {'first_and_last_name': 'Mr. FirstName LastName', 'address': 'Address', 'city': 'City State 12345',
                   'country': 'United States', 'phone': '1234567890'}
comment_text = "Test shopping"

def test_case_16_place_order_login_before_checkout(app):
    # CREATE NEW ACCOUNT
    app.automExercise.openUrl("https://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to('AutomationExercise')
    app.automExercise.click_login_signup_button()
    app.assert_that(app.automExercise.get_new_user_sign_up_text()).is_equal_to('New User Signup!')
    app.automExercise.set_sign_up_name_and_email('name', email)
    app.automExercise.click_sign_up_button()
    app.assert_that(app.automExercise.get_enter_account_information_text()).is_equal_to('ENTER ACCOUNT INFORMATION')
    app.automExercise.fill_account_information('Mr', 'TestName', password, '1/1/1990')
    app.automExercise.select_newsletter_and_special_offers()
    app.automExercise.fill_address_information('FirstName', 'LastName', 'Company', 'Address', 'Address2',
                                               'United States', 'State', 'City', '12345', '1234567890')
    app.automExercise.create_account()
    app.automExercise.click_continue_after_account_creation()
    app.automExercise.click_logout()

    # test_case_16_place_order_login_before_checkout
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_login_signup_button()
    app.automExercise.enter_correct_email_and_password(email, password)
    app.automExercise.click_login_button()
    app.assert_that(app.automExercise.verify_logged_in_user_display()).is_equal_to('Logged in as TestName')
    app.automExercise.click_add_to_cart_on_first_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_add_to_cart_on_third_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_cart_button()
    app.assert_that(app.automExercise.get_product_data("1")).is_equal_to(first)
    app.assert_that(app.automExercise.get_product_data("3")).is_equal_to(third)
    app.automExercise.click_proceed_to_checkout()
    app.assert_that(app.automExercise.get_details_delivery_address()).is_equal_to(delivery_address)
    app.assert_that(app.automExercise.get_details_billing_address()).is_equal_to(billing_address)
    app.assert_that(app.automExercise.get_product_data("1")).is_equal_to(first)
    app.assert_that(app.automExercise.get_product_data("3")).is_equal_to(third)
    app.automExercise.input_description_in_comment_text_area(comment_text)
    app.automExercise.click_place_order_button()
    app.automExercise.fill_payment_details('TestCard', '4780375202751048', '515', '11', '2025')
    app.automExercise.click_pay_and_confirm_order_button()
    app.automExercise.go_back()
    app.assert_that(app.automExercise.get_success_message_order_text()).is_equal_to("Your order has been placed successfully!")
    app.automExercise.click_pay_and_confirm_order_button()
    app.automExercise.delete_account()
    app.assert_that(app.automExercise.verify_account_deleted()).is_equal_to("ACCOUNT DELETED!")
    app.automExercise.click_continue_after_account_deleted()
