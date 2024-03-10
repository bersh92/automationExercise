def test_case_7_verify_test_cases_page(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_on_test_cases_button()
    app.automExercise.verify_user_is_navigated_to_test_cases_page_successfully()
