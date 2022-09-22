
import autoit
import time

from models.browser import Browser
from models.account import Account
from models.getconfig import Configure
import common as cons
import decorator

config = Configure()


class Project(object):

    def upload_td(self, td_tile):
        account = Account(config.username_correct, config.password_correct, config.verification_code)
        browser = account.login_with_verified()
        browser.find_element_click(xpath=cons.UPLOAD_TD_BUTTON)
        autoit.control_focus("文件上传", "[Class:Edit; instance:1]")
        autoit.control_set_text("文件上传", "[Class:Edit; instance:1]", td_tile)
        autoit.control_click("文件上传", "[Class:Button; instance:1]")
        time.sleep(cons.TIMEOUT_LONG)
        browser.find_element_click(1, className=cons.TD_UPLOAD_SUBMIT)


if __name__ =="__main__":
    project = Project()
    project.upload_td(cons.TD_FILE_1)


