from helpers.utils import Utils

email = Utils.generate_random_email()
password = "TestPassword"
first = {'title': 'Blue Top', 'price': 'Rs. 500', 'quantity': '1', 'total_price': 'Rs. 500'}
third = {'title': 'Sleeveless Dress', 'price': 'Rs. 1000', 'quantity': '1', 'total_price': 'Rs. 1000'}
delivery_address = {'first_and_last_name': 'Mr. Default User', 'address': '123 Default St',
                    'city': 'Los Angeles California 90001', 'country': 'United States', 'phone': '1234567890'}
billing_address = {'first_and_last_name': 'Mr. Default User', 'address': '123 Default St',
                   'city': 'Los Angeles California 90001', 'country': 'United States', 'phone': '1234567890'}
comment_text = "Test shopping"
name = 'Default Name'

def test_case_16_place_order_login_before_checkout(app):
    # CREATE NEW ACCOUNT
    Utils.create_account_with_defaults(email, password)

    # test_case_16_place_order_login_before_checkout
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_login_signup_button()
    app.automExercise.enter_correct_email_and_password(email, password)
    app.automExercise.click_login_button()
    app.assert_that(app.automExercise.verify_logged_in_user_display()).is_equal_to('Logged in as Default Name')
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
