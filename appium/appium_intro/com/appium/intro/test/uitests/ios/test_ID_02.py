import time

from selenium.webdriver.common.by import By

from com.appium.conrad.test.setup.devicedriver import DeviceDriver
from com.appium.conrad.test.utils import constants


# Test Case:
# 1. Open application
# 2. Click 'Login' button on Welcome page
# 3. Set user name in 'Username' field
# 4. Set user password in 'Password' field
# 5. Click 'LOGIN' button
def test_hybrid():
    # Start and get driver
    DeviceDriver().get_driver()
    driver = DeviceDriver().driver
    time.sleep(constants.WAIT_10_SECONDS)

    # Skip/close BE-Mobile ('Google info') popup by click 'OK' button
    _app_by_id = constants.ANDROID_PKG + constants.BY_ID

    btn_ok = driver.find_element(By.ID, _app_by_id + 'button1')
    btn_ok.click()

    # Get all contexts from application
    context_list = driver.contexts
    print context_list

    # Switch from [NATIVE] context to [WEBVIEW]
    # context_list[0] - it's [NATIVE_APP] context
    # context_list[1] - it's [WEBVIEW_android....] context
    # context_list[2] - it's [WEBVIEW_application....] context
    driver.switch_to.context(context_list[2])

    # Get current context after switch
    current = driver.current_context
    print current

    # Get 'innerHTML' from application to have all controls for future
    element = driver.find_element(By.XPATH, '/*')
    html = element.get_attribute('innerHTML')
    print '<' + element.tag_name + '>'
    print html
    print '<' + element.tag_name + '>'

    # Find elements from received HTML which will be used in out test case
    btn_login_from_marketing = driver.find_element(By.ID, 'btnLoginFromMarketing')
    btn_login = driver.find_element(By.ID, 'btnLogin')
    edt_username = driver.find_element(By.ID, 'txtUser')
    edt_password = driver.find_element(By.ID, 'txtPassword')

    # Verify that our controls are enabled on page
    print btn_login_from_marketing.is_enabled()
    print btn_login.is_enabled()
    print edt_username.is_enabled()
    print edt_password.is_enabled()

    # Login test case
    btn_login_from_marketing.click()
    edt_username.send_keys(constants.USER_GMAIL_EMAIL)
    edt_password.send_keys(constants.USER_GMAIL_PWD)
    btn_login.click()
    time.sleep(constants.WAIT_5_SECONDS)

    # Switch back to the [NATIVE] context if need
    driver.switch_to.context(context_list[0])

    # Close incorrect login popup by click 'OK' button
    btn_ok.click()

    # Close session
    DeviceDriver().quit()
