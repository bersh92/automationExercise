import time

first = {'title': 'Blue Top', 'price': 'Rs. 500', 'quantity': '1', 'total_price': 'Rs. 500'}
second = {'title': 'Men Tshirt', 'price': 'Rs. 400', 'quantity': '1', 'total_price': 'Rs. 400'}

def test_case_17_remove_products_from_cart(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_add_to_cart_on_first_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_add_to_cart_on_second_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_cart_button()
    app.assert_that(app.automExercise.get_product_data("1")).is_equal_to(first)
    app.assert_that(app.automExercise.get_product_data("2")).is_equal_to(second)
    app.automExercise.click_x_button_product_from_cart("1")
    app.assert_that(app.automExercise.check_product_displaying_in_cart('Blue Top')).is_equal_to(False)
    app.assert_that(app.automExercise.get_names_products_are_added_to_cart()).is_equal_to(['Men Tshirt'])
