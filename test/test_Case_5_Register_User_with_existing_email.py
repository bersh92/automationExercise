from helpers.utils import Utils

email = Utils.generate_random_email()
password = "TestPassword"
name = 'Default Name'

def test_case_5_register_user_with_existing_email(app):
    # CREATE NEW ACCOUNT
    Utils.create_account_with_defaults(email, password)

    #test_case_5_register_user_with_existing_email
    app.automExercise.openUrl("https://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to('AutomationExercise')
    app.automExercise.click_login_signup_button()
    app.assert_that(app.automExercise.get_new_user_sign_up_text()).is_equal_to("New User Signup!")
    app.automExercise.set_sign_up_name_and_email("name", email)
    app.automExercise.click_sign_up_button()
    app.assert_that(app.automExercise.get_email_address_already_exist()).is_equal_to("Email Address already exist!")
