from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from appium_intro.com.appium.intro.test.setup.devicedriver import DeviceDriver
from appium_intro.com.appium.intro.test.utils import constants


class Controls(object):
    def __init__(self):
        self.driver = DeviceDriver().driver
        self.wait = WebDriverWait(self.driver, constants.WAIT_7_SECONDS)

    # Find element located by XPATH
    def find_element_located_by_xpath(self, value=None):
        self.wait.until(EC.visibility_of_element_located(value))
        return self.driver.find_element_by_xpath(value[1])

    # Find element clickable by XPATH
    def find_element_clickable_by_xpath(self, value=None):
        self.wait.until(EC.element_to_be_clickable(value))
        return self.driver.find_element_by_xpath(value[1])

    # Find element located by ID
    def find_element_located_by_id(self, value=None):
        self.wait.until(EC.visibility_of_element_located(value))
        return self.driver.find_element_by_id(value[1])

    # Find elements located by ID
    def find_elements_located_by_id(self, value=None):
        self.wait.until(EC.visibility_of_element_located(value))
        return self.driver.find_elements_by_id(value[1])

    # Find element clickable by ID
    def find_element_clickable_by_id(self, value=None):
        self.wait.until(EC.element_to_be_clickable(value))
        return self.driver.find_element_by_id(value[1])

    # Verify that element is visible in DOM
    def verify_exists_of_element(self, value=None):
        return self.driver.find_elements(value[0], value[1])
