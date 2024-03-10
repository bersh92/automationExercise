import time

from helpers.utils import Utils

second = {'title': 'Men Tshirt', 'price': 'Rs. 400', 'quantity': '1', 'total_price': 'Rs. 400'}
third = {'title': 'Sleeveless Dress', 'price': 'Rs. 1000', 'quantity': '1', 'total_price': 'Rs. 1000'}
random_email = Utils.generate_random_email()
delivery_address = {'first_and_last_name': 'Mrs. TestName LastName', 'address': 'Address', 'city': 'City State 4578950', 'country': 'Canada', 'phone': '583063041800'}
billing_address = {'first_and_last_name': 'Mrs. TestName LastName', 'address': 'Address', 'city': 'City State 4578950', 'country': 'Canada', 'phone': '583063041800'}
comment_text = "Test shopping"

def test_case_14_place_order_Register_while_Checkout(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_add_to_cart_on_second_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_add_to_cart_on_third_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_cart_button()
    app.assert_that(app.automExercise.get_product_data("2")).is_equal_to(second)
    app.assert_that(app.automExercise.get_product_data("3")).is_equal_to(third)
    app.automExercise.click_proceed_to_checkout()
    app.automExercise.click_register_login_button()
    app.automExercise.set_sign_up_name_and_email('TestName', random_email)
    app.automExercise.click_sign_up_button()
    app.automExercise.fill_account_information('Mrs', 'TestName', 'TestPassword', '1/3/1991')
    app.automExercise.select_newsletter_and_special_offers()
    app.automExercise.fill_address_information('TestName', 'LastName', 'Company', 'Address', 'Address2', 'Canada', 'State', 'City', '4578950', '583063041800')
    app.automExercise.create_account()
    app.assert_that(app.automExercise.verify_account_created()).is_equal_to('ACCOUNT CREATED!')
    app.automExercise.click_continue_after_account_creation()
    app.assert_that(app.automExercise.verify_logged_in_user_display()).is_equal_to('Logged in as TestName')
    app.automExercise.click_cart_button()
    app.automExercise.click_proceed_to_checkout()
    app.assert_that(app.automExercise.get_details_delivery_address()).is_equal_to(delivery_address)
    app.assert_that(app.automExercise.get_details_billing_address()).is_equal_to(billing_address)
    app.assert_that(app.automExercise.get_product_data("2")).is_equal_to(second)
    app.assert_that(app.automExercise.get_product_data("3")).is_equal_to(third)
    app.automExercise.input_description_in_comment_text_area(comment_text)
    app.automExercise.click_place_order_button()
    app.automExercise.fill_payment_details('TestCard', '9785365203751048', '534', '12', '2025')
    app.automExercise.click_pay_and_confirm_order_button()
    app.assert_that(app.automExercise.get_success_message_your_order_has_been_placed_successfully()).is_equal_to('Your order has been placed successfully!')
    app.automExercise.delete_account()
    app.assert_that(app.automExercise.verify_account_deleted()).is_equal_to('ACCOUNT DELETED!')