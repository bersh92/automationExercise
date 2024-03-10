search_text = "Jeans"
list_search_products = ["Soft Stretch Jeans", "Regular Fit Straight Jeans", "Grunt Blue Slim Fit Jeans"]

def test_case_9_search_product(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_on_products_button()
    app.automExercise.verify_user_is_navigated_to_all_products_page_successfully()
    app.automExercise.enter_product_name_in_search_input(search_text)
    app.automExercise.click_search_button()
    app.assert_that(app.automExercise.get_all_product_names_related_to_search_are_visible()).is_equal_to(list_search_products)

