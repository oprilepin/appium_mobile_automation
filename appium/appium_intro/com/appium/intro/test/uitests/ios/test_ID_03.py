import unittest

from com.appium.conrad.test.pages.activationpage import ActivationPage
from com.appium.conrad.test.pages.composepage import ComposePage
from com.appium.conrad.test.pages.mainpage import MainPage
from com.appium.conrad.test.pages.searchpage import SettingsPage
from com.appium.conrad.test.pages.signinpage import SignInPage
from com.appium.conrad.test.pages.welcomepage import WelcomePage
from com.appium.conrad.test.setup.devicedriver import DeviceDriver
from com.appium.conrad.test.utils import constants


class TestSuiteSignIn(unittest.TestCase):
    def setUp(self):
        DeviceDriver.get_driver()

    def test_check_welcome_page(self):
        welcomes = WelcomePage()
        welcomes.verify_welcome_page_question()
        welcomes.verify_gmail_apps_btn()
        welcomes.verify_exchange_btn()
        welcomes.verify_other_email_btn()

    def test_sign_in_as_exchange_account_negative(self):
        welcomes = WelcomePage()
        welcomes.click_exchange_btn()
        signin = SignInPage()
        signin.set_acc_name(constants.USER_GMAIL_NAME)
        signin.set_acc_email(constants.USER_GMAIL_EMAIL)
        signin.set_acc_password(constants.USER_GMAIL_PWD)
        signin.click_activate_btn()
        signin.verify_manual_acc_setup_msg()
        signin.verify_manual_acc_setup_info(constants.MANUAL_SETUP_MSG_INFO)
        signin.click_ok_btn()

    def test_sign_in_as_other_account_and_send_email(self):
        welcomes = WelcomePage()
        welcomes.click_other_email_btn()
        signin = SignInPage()
        signin.set_acc_name(constants.USER_AOL_NAME)
        signin.set_acc_email(constants.USER_AOL_EMAIL)
        signin.set_acc_password(constants.USER_AOL_PWD)
        signin.click_activate_btn()
        activate = ActivationPage()
        activate.verify_activating_title()
        activate.click_go_to_inbox_btn()
        main = MainPage()
        main.open_secure_compose()
        compose = ComposePage()
        compose.skip_tutorial()
        compose.compose_message(constants.USER_GMAIL_EMAIL, constants.SUBJECT, constants.BODY)
        compose.click_send_btn()
        compose.verify_encrypt_progress()

    def test_go_to_dashboard(self):
        welcomes = WelcomePage()
        welcomes.click_other_email_btn()
        signin = SignInPage()
        signin.set_acc_name(constants.USER_AOL_NAME)
        signin.set_acc_email(constants.USER_AOL_EMAIL)
        signin.set_acc_password(constants.USER_AOL_PWD)
        signin.click_activate_btn()
        activate = ActivationPage()
        activate.verify_activating_title()
        activate.click_go_to_inbox_btn()
        main = MainPage()
        main.open_dashboard()

    def test_sign_in_as_gmail_account_with_remove(self):
        welcomes = WelcomePage()
        welcomes.click_gmail_btn()
        signin = SignInPage()
        signin.select_google_account()
        signin.verify_attempt_server_settings_message()
        activate = ActivationPage()
        activate.verify_activating_title()
        activate.click_go_to_inbox_btn()
        main = MainPage()
        main.open_sent_folder()
        main.open_settings()
        settings = SettingsPage()
        settings.delete_acc_btn()

    def tearDown(self):
        DeviceDriver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuiteSignIn)
    unittest.TextTestRunner(verbosity=1).run(suite)
