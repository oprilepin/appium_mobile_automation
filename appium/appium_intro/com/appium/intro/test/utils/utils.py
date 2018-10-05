from selenium.webdriver.support.wait import WebDriverWait

from appium_intro.com.appium.intro.test.setup.devicedriver import DeviceDriver
from appium_intro.com.appium.intro.test.utils import constants


class DeviceDriverUtils(object):
    def __init__(self):
        self.driver = DeviceDriver().driver
        self.wait = WebDriverWait(self.driver, constants.WAIT_5_SECONDS)

    def switch_to_native_context(self):
        self.driver.switch_to.context('NATIVE_APP')

    def switch_to_webview_context(self):
        if not self.driver.context or self.driver.context == "NATIVE_APP":
            switch_to = 'WEBVIEW_' + constants.ANDROID_PKG
            self.driver.switch_to.context(switch_to)

    def swipe_right_horizontal(self, height):
        h = {'menu': 5, 'product': 2}
        # Get the size of screen
        size = self.driver.get_window_size()

        # Find 'start_x' point which is at right side of screen
        start_x = size['width'] * 0.7

        # Find 'end_x' point which is at left side of screen
        end_x = size['width'] * 0.3

        # Find vertical point where you wants to swipe. It is in middle of screen height

        start_y = size['height'] / h[height]

        # Swipe from Right to Left
        self.driver.swipe(start_x, start_y, end_x, start_y, 300)

    def swipe_left_horizontal(self, height):
        h = {'menu': 5, 'product': 2}

        # Get the size of screen
        size = self.driver.get_window_size()

        # Find 'start_x' point which is at right side of screen
        start_x = size['width'] * 0.7

        # Find 'end_x' point which is at left side of screen
        end_x = size['width'] * 0.3

        # Find vertical point where you wants to swipe. It is in middle of screen height
        start_y = size['height'] / h[height]

        # Swipe from Left to Right
        self.driver.swipe(end_x, start_y, start_x, start_y, 300)

    def swipe_down_vertical(self):
        # Get the size of screen
        size = self.driver.get_window_size()

        # Find 'start_y' point which is at bottom side of screen
        start_y = size['height'] * 0.4
        # start_y = size['height'] * 0.5

        # Find 'end_y' point which is at top side of screen
        end_y = size['height'] * 0.2

        # Find horizontal point where you wants to swipe. It is in middle of screen width
        start_x = size['width'] / 2

        # Swipe from Bottom to Top
        self.driver.swipe(start_x, start_y, start_x, end_y, 300)

    def swipe_down_vertical_long(self):
        # Get the size of screen
        size = self.driver.get_window_size()

        # Find 'start_y' point which is at bottom side of screen
        start_y = size['height'] * 0.8

        # Find 'end_y' point which is at top side of screen
        end_y = size['height'] * 0.2

        # Find horizontal point where you wants to swipe. It is in middle of screen width
        start_x = size['width'] / 2

        # Swipe from Bottom to Top
        self.driver.swipe(start_x, start_y, start_x, end_y, 300)

    def swipe_up_vertical_short(self):
        # Get the size of screen
        size = self.driver.get_window_size()

        # Find 'start_y' point which is at bottom side of screen
        start_y = size['height'] * 0.8

        # Find 'end_y' point which is at top side of screen
        end_y = size['height'] * 0.6

        # Find horizontal point where you wants to swipe. It is in middle of screen width
        start_x = size['width'] / 2

        # Swipe from Top to Bottom
        self.driver.swipe(start_x, end_y, start_x, start_y, 200)

    def swipe_up_vertical(self):
        # Get the size of screen
        size = self.driver.get_window_size()

        # Find 'start_y' point which is at bottom side of screen
        start_y = size['height'] * 0.4

        # Find 'end_y' point which is at top side of screen
        end_y = size['height'] * 0.2

        # Find horizontal point where you wants to swipe. It is in middle of screen width
        start_x = size['width'] / 2

        # Swipe from Top to Bottom
        self.driver.swipe(start_x, start_y, start_x, end_y, 100)
