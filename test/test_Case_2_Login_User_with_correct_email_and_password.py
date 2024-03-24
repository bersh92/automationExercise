from helpers.utils import Utils

email = Utils.generate_random_email()
password = "TestPassword"
name = 'Default Name'

def test_case_2_login_user_with_correct_email_and_password(app):
    # CREATE NEW ACCOUNT
    Utils.create_account_with_defaults(email, password)

    # test_case_2_login_user_with_correct_email_and_password
    app.automExercise.openUrl("https://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to('AutomationExercise')
    app.automExercise.click_login_signup_button()
    app.assert_that(app.automExercise.get_login_to_your_account_text()).is_equal_to("Login to your account")
    app.automExercise.enter_correct_email_and_password(email, password)
    app.automExercise.click_login_button()
    app.assert_that(app.automExercise.verify_logged_in_user_display()).is_equal_to(f'Logged in as {name}')
    app.automExercise.delete_account()
    app.assert_that(app.automExercise.verify_account_deleted()).is_equal_to('ACCOUNT DELETED!')
