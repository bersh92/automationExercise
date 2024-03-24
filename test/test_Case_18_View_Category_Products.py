categories = ['WOMEN', 'MEN', 'KIDS']

def test_case_18_view_category_products(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_list_categories_text()).is_equal_to(categories)
    app.automExercise.click_category_women()
    app.automExercise.click_category_women_tops()
    app.assert_that(app.automExercise.get_text_women_tops_products()).is_equal_to("WOMEN - TOPS PRODUCTS")
    app.automExercise.click_category_men_button()
    app.automExercise.click_category_men_jeans()
    app.assert_that(app.automExercise.get_text_men_jeans_products()).is_equal_to("MEN - JEANS PRODUCTS")