#! /usr/bin/env python

import time
import selenium.common.exceptions as exc
from selenium.webdriver.common.keys import Keys

from models.browser import Browser
from models.getconfig import Configure
import common as cons

config = Configure()


class Account(object):
    def __init__(self, username, password, verification_code):
        self.username = username
        self.password = password
        self.verification_code = verification_code

    def login_with_verified(self):
        browser = self.login_before_verify()
        browser.find_element_click(xpath=cons.GET_VERIFI_CODE)
        browser.find_element_sendkeys(config.verification_code, xpath=cons.VERIFICATION_CODE_INPUT_BOX)
        browser.find_element_click(xpath=cons.VERIFI_PAGE_CONFIRM)
        time.sleep(cons.TIMEOUT_SHORT)
        new_browser = browser.switch_window()
        current_page = browser.current_url(new_browser)
        if current_page == cons.PROJECT_PAGE:
            print("登录成功")
            return browser
        else:
            print("登录失败")
            browser.close_browser()
            return False

    def get_login_message(self):
        browser = self.login_before_verify()
        message = ''
        for element in cons.LOG_ERROR_MESSAGE.split("|"):
            time.sleep(cons.TIMEOUT_SHORT)
            message = browser.find_element_getText(className=element)
            if message:
                browser.close_browser()
                return message
        if not message:
            time.sleep(cons.TIMEOUT_SHORT)
            message = browser.find_element_getText(className=cons.LOG_VERIFY_DIALOG)
        browser.close_browser()
        return message

    def login_before_verify(self):
        browser = Browser()
        browser.open_url(cons.LOGIN_PAGE)
        browser.find_element_sendkeys(self.username, name=cons.USERNAME)
        browser.send_keyboard_key(Keys.TAB, name=cons.USERNAME)
        browser.find_element_sendkeys(self.password, name=cons.PASSWORD)
        browser.send_keyboard_key(Keys.TAB, name=cons.PASSWORD)
        browser.find_element_click(xpath=cons.LOGIN_BUTTON)
        return browser


if __name__ == "__main__":
    account = Account(config.username_correct, config.password_correct, config.verification_code)
    print(account.get_login_message())
