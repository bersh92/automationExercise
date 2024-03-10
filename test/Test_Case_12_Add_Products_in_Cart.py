import time
list_products_added_to_cart = ["Blue Top", "Men Tshirt"]
first = {'title': 'Blue Top', 'price': 'Rs. 500', 'quantity': '1', 'total_price': 'Rs. 500'}
second = {'title': 'Men Tshirt', 'price': 'Rs. 400', 'quantity': '1', 'total_price': 'Rs. 400'}

def test_case_12_add_products_in_cart(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_on_products_button()
    app.automExercise.click_add_to_cart_on_first_product()
    app.automExercise.click_continue_shopping_button()
    app.automExercise.click_add_to_cart_on_second_product()
    app.automExercise.click_view_cart_button()
    app.assert_that(app.automExercise.get_product_data("1")).is_equal_to(first)
    app.assert_that(app.automExercise.get_product_data("2")).is_equal_to(second)