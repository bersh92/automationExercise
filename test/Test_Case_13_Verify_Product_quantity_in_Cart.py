import time
product_detail = {'name_product': 'Sleeveless Dress', 'category': 'Category: Women > Dress', 'price': 'Rs. 1000', 'brand': 'Brand: Madame'}
quantity = "4"
product_is_displayed_in_cart_page_with_exact_quantity = {'title': 'Sleeveless Dress', 'price': 'Rs. 1000', 'quantity': '4', 'total_price': 'Rs. 4000'}


def test_case_13_verify_product_quantity_in_cart(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_on_view_product_of_third_product()
    app.assert_that(app.automExercise.get_product_detail_is_opened()).is_equal_to(product_detail)
    app.automExercise.input_quantity(quantity)
    app.automExercise.click_add_to_cart_button()
    app.automExercise.click_view_cart_button()
    app.assert_that(app.automExercise.get_product_data("3")).is_equal_to(product_is_displayed_in_cart_page_with_exact_quantity)
