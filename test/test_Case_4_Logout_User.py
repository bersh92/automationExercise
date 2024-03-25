from helpers.utils import Utils

email = Utils.generate_random_email()
password = "TestPassword"
name = 'Default Name'

def test_case_4_logout_user(app):
    # CREATE NEW ACCOUNT
    Utils.create_account_with_defaults(email, password)

    # test_case_4_logout_user
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_login_signup_button()
    app.assert_that(app.automExercise.get_login_to_your_account_text()).is_equal_to("Login to your account")
    app.automExercise.enter_correct_email_and_password(email, password)
    app.automExercise.click_login_button()
    app.assert_that(app.automExercise.verify_logged_in_user_display()).is_equal_to("Logged in as Default Name")
    app.automExercise.click_logout()
    app.automExercise.verify_that_user_is_navigated_to_login_page()

