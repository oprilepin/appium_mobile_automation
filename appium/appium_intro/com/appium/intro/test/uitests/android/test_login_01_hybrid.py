# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from appium_intro.com.appium.intro.test.pages.mainpage import MainPage
from appium_intro.com.appium.intro.test.setup.devicedriver import DeviceDriver


def test_cart_page_04():
    driver = DeviceDriver().get_driver()
    mainpage = MainPage()
    time.sleep(4)
    mainpage.click_ok_btn()
    context_list = driver.contexts
    print(context_list)
    print(context_list[0])
    print(context_list[1])
    driver.switch_to.context(context_list[1])

    current = driver.current_context
    print(current)

    element = driver.find_element(By.XPATH, '/*')
    html = element.get_attribute('innerHTML')
    print('<' + element.tag_name + '>')
    print(html)
    print('<' + element.tag_name + '>')
    btn_login_from_marketing = driver.find_element(By.ID, 'btnLoginFromMarketing')
    btn_login_from_marketing.click()

    time.sleep(4)
    driver.quit()



def test_cart_page_043():
    driver = DeviceDriver().get_driver()
    mainpage = MainPage()
    time.sleep(4)
    mainpage.click_ok_btn()


    driver.switch_to.context("WEBVIEW_com.bei.bemobile")

    element = driver.find_element(By.XPATH, '/*')
    html = element.get_attribute('innerHTML')
    print('<' + element.tag_name + '>')
    print(html)
    print('<' + element.tag_name + '>')
    btn_login_from_marketing = driver.find_element(By.ID, 'btnLoginFromMarketing')
    btn_login_from_marketing.click()

    driver.switch_to.context("NATIVE_APP")

    time.sleep(4)
    driver.quit()
