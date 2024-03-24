from helpers.utils import Utils

random_email = Utils.generate_random_email()
first = {'title': 'Blue Top', 'price': 'Rs. 500', 'quantity': '1', 'total_price': 'Rs. 500'}
second = {'title': 'Men Tshirt', 'price': 'Rs. 400', 'quantity': '1', 'total_price': 'Rs. 400'}
delivery_address = {'first_and_last_name': 'Mrs. TestName LastName', 'address': 'Address', 'city': 'City State 4578950',
                    'country': 'Canada', 'phone': '583063041800'}
billing_address = {'first_and_last_name': 'Mrs. TestName LastName', 'address': 'Address', 'city': 'City State 4578950',
                   'country': 'Canada', 'phone': '583063041800'}
comment_text = "Test shopping"


def test_case_15_place_order_register_before_checkout(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_login_signup_button()
    app.automExercise.set_sign_up_name_and_email('TestName', random_email)
    app.automExercise.click_sign_up_button()
    app.automExercise.fill_account_information('Mrs', 'TestName', 'TestPassword', '1/3/1991')
    app.automExercise.select_newsletter_and_special_offers()
    app.automExercise.fill_address_information('TestName', 'LastName', 'Company', 'Address', 'Address2', 'Canada',
                                               'State', 'City', '4578950', '583063041800')
    app.automExercise.create_account()
    app.assert_that(app.automExercise.verify_account_created()).is_equal_to('ACCOUNT CREATED!')
    app.automExercise.click_continue_after_account_creation()
    app.assert_that(app.automExercise.verify_logged_in_user_display()).is_equal_to('Logged in as TestName')
    app.automExercise.click_add_to_cart_on_first_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_add_to_cart_on_second_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_cart_button()
    app.assert_that(app.automExercise.get_product_data("1")).is_equal_to(first)
    app.assert_that(app.automExercise.get_product_data("2")).is_equal_to(second)
    app.automExercise.click_proceed_to_checkout()
    app.assert_that(app.automExercise.get_details_delivery_address()).is_equal_to(delivery_address)
    app.assert_that(app.automExercise.get_details_billing_address()).is_equal_to(billing_address)
    app.assert_that(app.automExercise.get_product_data("1")).is_equal_to(first)
    app.assert_that(app.automExercise.get_product_data("2")).is_equal_to(second)
    app.automExercise.input_description_in_comment_text_area(comment_text)
    app.automExercise.click_place_order_button()
    app.automExercise.fill_payment_details('TestCard', '1780365202751048', '312', '11', '2026')
    app.automExercise.click_pay_and_confirm_order_button()
    app.automExercise.go_back()
    app.assert_that(app.automExercise.get_success_message_order_text()).is_equal_to("Your order has been placed successfully!")
    app.automExercise.click_pay_and_confirm_order_button()
    app.automExercise.delete_account()
    app.assert_that(app.automExercise.verify_account_deleted()).is_equal_to("ACCOUNT DELETED!")
    app.automExercise.click_continue_after_account_deleted()
