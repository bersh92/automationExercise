email = "testing@gmail.com"

def test_case_10_verify_subscription_in_home_page(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.step.scroll_page('bottom')
    app.assert_that(app.automExercise.get_subscription_text()).is_equal_to("SUBSCRIPTION")
    app.automExercise.enter_email_address_in_input(email)
    app.automExercise.click_arrow_button_subscription()
    app.assert_that(app.automExercise.get_success_message_subscribed()).is_equal_to("You have been successfully subscribed!")



