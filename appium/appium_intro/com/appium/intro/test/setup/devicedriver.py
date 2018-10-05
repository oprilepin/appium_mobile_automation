from appium import webdriver
from appium_intro.com.appium.intro.test.utils import constants


class DeviceDriver():
    @staticmethod
    def set_driver():

        desired_caps = {
            'automationName': constants.AUTOMATION_NAME,
            'platformName': constants.PLATFORM_NAME,
            'deviceName': constants.DEVICE_NAME,
            'app': constants.APP_NAME,
            'noReset': constants.APP_RESET
        }
        try:
            DeviceDriver.driver = webdriver.Remote(constants.HOST, desired_caps)
        except Exception as e:
            raise e

        return DeviceDriver.driver

    @staticmethod
    def get_driver():
        return DeviceDriver.set_driver()

    @staticmethod
    def quit():
        DeviceDriver.driver.quit()
