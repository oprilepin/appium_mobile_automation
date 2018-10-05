# -*- coding: utf-8 -*-
import time

from appium_intro.com.appium.intro.test.pages.mainpage import MainPage
from appium_intro.com.appium.intro.test.setup.devicedriver import DeviceDriver


def test_cart_page_04():
    driver = DeviceDriver().get_driver()
    mainpage = MainPage()
    # time.sleep(4)
    mainpage.click_ok_btn()
    context_list = driver.contexts
    print(context_list)
    current = driver.current_context
    print(current)
    driver.quit()
