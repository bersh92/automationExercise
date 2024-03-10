import time

name = "TestName"
email = "T4snaIl0i0myyaa1@example.com"
subject = "Contact from testing."
message = "The feedback form is being tested"

def test_case_6_contact_us_form(app):
    app.automExercise.openUrl("http://automationexercise.com/")
    app.assert_that(app.automExercise.get_automation_experience_text()).is_equal_to("AutomationExercise")
    app.automExercise.click_on_contact_us_button()
    app.assert_that(app.automExercise.get_get_in_touch_text()).is_equal_to("GET IN TOUCH")
    app.automExercise.set_contact_us_get_in_touch_name_email_subject_and_message(name, email, subject, message)
    app.automExercise.upload_the_file()
    app.automExercise.click_submit_button()
    app.automExercise.confirm_upload()
    app.assert_that(app.automExercise.get_success_your_details_have_been_submitted_successfully_text()).is_equal_to("Success! Your details have been submitted successfully.")
    app.automExercise.click_home_button()
    app.automExercise.verify_that_landed_to_home_page_successfully()
