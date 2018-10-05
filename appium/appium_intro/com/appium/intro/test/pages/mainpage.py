from selenium.webdriver.common.by import By

from appium_intro.com.appium.intro.test.controls.controls import Controls
from appium_intro.com.appium.intro.test.setup.devicedriver import DeviceDriver
from appium_intro.com.appium.intro.test.utils import constants
from appium_intro.com.appium.intro.test.utils.utils import DeviceDriverUtils


class MainPage(object):
    def __init__(self):
        self.driver = DeviceDriver.driver

    _app_by_id = constants.APP_PKG + constants.BY_ID
    _android_by_id = constants.ANDROID_PKG + constants.BY_ID

    _btn_search = (By.ID, _app_by_id + 'menu_action_search')
    _btn_ok = (By.ID, _android_by_id + 'button1')
    _btn_cancel = (By.ID, _android_by_id + 'button2')

    # Click OK btn
    def click_ok_btn(self):
        if Controls().find_element_located_by_id(self._btn_ok).is_displayed():
            Controls().find_element_located_by_id(self._btn_ok).click()

    # Click Cancel btn
    def click_cancel_btn(self):
        Controls().find_element_located_by_id(self._btn_cancel).click()

