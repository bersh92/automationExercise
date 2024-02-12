
email = "testing@gmail.com"
password = "testing06"

def test_Case_3_login_user_with_incorrect_email_and_password(app):
    app.automExercise.openUrl("https://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to('AutomationExercise')
    app.automExercise.click_login_signup_button()
    app.assert_that(app.automExercise.get_login_to_your_account_text()).is_equal_to('Login to your account')
    app.automExercise.enter_incorrect_email_and_password(email, password)
    app.automExercise.click_login_button()
    app.assert_that(app.automExercise.get_your_email_or_password_is_incorrect()).is_equal_to('Your email or password is incorrect!')