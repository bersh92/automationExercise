list_of_products = ['Blue Top', 'Men Tshirt', 'Sleeveless Dress', 'Stylish Dress', 'Winter Top', 'Summer White Top', 'Madame Top For Women', 'Fancy Green Top', 'Sleeves Printed Top - White', 'Half Sleeves Top Schiffli Detailing - Pink', 'Frozen Tops For Kids', 'Full Sleeves Top Cherry - Pink', 'Printed Off Shoulder Top - White', 'Sleeves Top and Short - Blue & Pink', 'Little Girls Mr. Panda Shirt', 'Sleeveless Unicorn Patch Gown - Pink', 'Cotton Mull Embroidered Dress', 'Blue Cotton Indie Mickey Dress', 'Long Maxi Tulle Fancy Dress Up Outfits -Pink', 'Sleeveless Unicorn Print Fit & Flare Net Dress - Multi', 'Colour Blocked Shirt – Sky Blue', 'Pure Cotton V-Neck T-Shirt', 'Green Side Placket Detail T-Shirt', 'Premium Polo T-Shirts', 'Pure Cotton Neon Green Tshirt', 'Soft Stretch Jeans', 'Regular Fit Straight Jeans', 'Grunt Blue Slim Fit Jeans', 'Rose Pink Embroidered Maxi Dress', 'Cotton Silk Hand Block Print Saree', 'Rust Red Linen Saree', 'Beautiful Peacock Blue Cotton Linen Saree', 'Lace Top For Women', 'GRAPHIC DESIGN MEN T SHIRT - BLUE', '', '', '', 'Stylish Dress', 'Winter Top', 'Summer White Top']

def test_case_8_verify_all_products_and_product_detail_page(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_on_products_button()
    app.automExercise.verify_user_is_navigated_to_all_products_page_successfully()
    # app.assert_that(app.automExercise.get_products_names()).is_equal_to(list_of_products)
    app.automExercise.click_on_view_product_of_first_product()
    app.assert_that(app.automExercise.get_product_name()).is_equal_to("Blue Top")
    app.assert_that(app.automExercise.get_product_category()).is_equal_to("Category: Women > Tops")
    app.assert_that(app.automExercise.get_product_price()).is_equal_to("Rs. 500")
    app.assert_that(app.automExercise.get_product_availability()).is_equal_to("Availability: In Stock")
    app.assert_that(app.automExercise.get_product_condition()).is_equal_to("Condition: New")
    app.assert_that(app.automExercise.get_product_brand()).is_equal_to("Brand: Polo")
