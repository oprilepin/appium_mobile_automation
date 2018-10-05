import os

# Desire Capabilities
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_NAME = BASE_DIR + '//apps//BEM_v3.8.0.apk'
DEVICE_NAME = 'emulator-5554'
AUTOMATION_NAME = 'Appium'
PLATFORM_NAME = 'Android'
APP_RESET = 'False'
HOST = 'http://localhost:4723/wd/hub'

# Packages
APP_PKG = 'com.bei.bemobile'
ANDROID_PKG = 'android'

# Locators
BY_ID = ':id/'

# Waits
WAIT_1_SECOND = 1
WAIT_2_SECOND = 2
WAIT_5_SECONDS = 5
WAIT_7_SECONDS = 7
WAIT_10_SECONDS = 10

