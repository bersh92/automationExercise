from helpers.utils import Utils

email = Utils.generate_random_email()
password = "TestPassword"

def test_case_5_register_user_with_existing_email(app):
    # CREATE NEW ACCOUNT
    app.automExercise.openUrl("https://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to('AutomationExercise')
    app.automExercise.click_login_signup_button()
    app.assert_that(app.automExercise.get_new_user_sign_up_text()).is_equal_to('New User Signup!')
    app.automExercise.set_sign_up_name_and_email('name', email)
    app.automExercise.click_sign_up_button()
    app.assert_that(app.automExercise.get_enter_account_information_text()).is_equal_to('ENTER ACCOUNT INFORMATION')
    app.automExercise.fill_account_information('Mr', 'TestName', password, '1/1/1990')
    app.automExercise.select_newsletter_and_special_offers()
    app.automExercise.fill_address_information('FirstName', 'LastName', 'Company', 'Address', 'Address2',
                                               'United States', 'State', 'City', '12345', '1234567890')
    app.automExercise.create_account()
    app.automExercise.click_continue_after_account_creation()
    app.automExercise.click_logout()

    #test_case_5_register_user_with_existing_email
    app.automExercise.openUrl("https://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to('AutomationExercise')
    app.automExercise.click_login_signup_button()
    app.assert_that(app.automExercise.get_new_user_sign_up_text()).is_equal_to("New User Signup!")
    app.automExercise.set_sign_up_name_and_email("name", email)
    app.automExercise.click_sign_up_button()
    app.assert_that(app.automExercise.get_email_address_already_exist()).is_equal_to("Email Address already exist!")
