brands = ['(6)\nPOLO', '(5)\nH&M', '(5)\nMADAME', '(3)\nMAST & HARBOUR', '(4)\nBABYHUG', '(3)\nALLEN SOLLY JUNIOR',
          '(3)\nKOOKIE KIDS', '(5)\nBIBA']
brand_name_hm = ['Men Tshirt', 'Summer White Top', 'Pure Cotton V-Neck T-Shirt', 'Pure Cotton Neon Green Tshirt',
                  'Regular Fit Straight Jeans']
brand_name_babyhug = ['Sleeves Printed Top - White', 'Half Sleeves Top Schiffli Detailing - Pink',
                      'Printed Off Shoulder Top - White', 'Sleeves Top and Short - Blue & Pink']

def test_case_19_view_and_cart_brand_products(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.automExercise.click_on_products_button()
    app.assert_that(app.automExercise.get_list_brands_text()).is_equal_to(brands)
    app.automExercise.click_on_any_brand_name("H&M")
    app.assert_that(app.automExercise.get_products_names()).is_equal_to(brand_name_hm)
    app.automExercise.click_on_any_brand_name("Babyhug")
    app.assert_that(app.automExercise.get_products_names()).is_equal_to(brand_name_babyhug)