#! /usr/bin/env python
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from models.getconfig import Configure
import common as cons

config = Configure()


class Browser(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.main_window = self.driver.current_window_handle

    ''' 打开url页面
    |- args:
       url:   需要打开的url页面地址；
    '''
    def open_url(self, url):
        self.driver.get(url)

    ''' 关闭浏览器
    |- args: 无
    '''
    def close_browser(self):
        time.sleep(cons.TIMEOUT_SHORT)
        # self.driver.close()
        self.driver.quit()

    def switch_window(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        return self.driver

    def current_url(self, driver):
        return driver.current_url

    ''' 定义元素获取text数据
    |- args: 
      kwargs: type=element; type为：name, id, xpath, className等, element为对应值
    '''
    def find_element_getText(self, **kwargs):
        for type, element in kwargs.items():
            find_results = self.find_element_function(type, element)
            # className为多行文字返回时，对文字做拼接处理
            if isinstance(find_results, list):
                content = ''
                for i in range(len(find_results)):
                    content += find_results[i].text
                return content
            else:
                return False

    ''' 定义元素sendkeys
        |- args: 
          value:  sendkeys 发送的值;
          kwargs: type=element; type为：name, id, xpath, className等, element为对应值
    '''
    def find_element_sendkeys(self, value, **kwargs):
        for type, element in kwargs.items():
            if self.find_element_function(type, element):
                return self.find_element_function(type, element).send_keys(value)
            else:
                return False

    ''' 定义元素执行click操作
       |- args: 
         index:  如果找到的元素为list，index为点击的index, 默认为0;
         kwargs: type=element; type为：name, id, xpath, className等, element为对应值
    '''
    def find_element_click(self, index=0, **kwargs):
        for type, element in kwargs.items():
            find_result = self.find_element_function(type, element)
            if find_result:
                if isinstance(find_result, list):
                    return self.find_element_function(type, element)[index].click()
                else:
                    return self.find_element_function(type, element).click()
            else:
                return False


    '''根据type, element定义元素
    |- args: 
       type:    元素定位类型，id, name, xpath, className;
       element: 元素值;
    '''
    def find_element_function(self, type, element):
        try:
            if type.lower() == cons.ID.lower(): return self.driver.find_element_by_id(element)
            if type.lower() == cons.XPATH.lower(): return self.driver.find_element_by_xpath(element)
            if type.lower() == cons.NAME.lower(): return self.driver.find_element_by_name(element)
            if type.lower() == cons.CLASSNAME.lower(): return self.driver.find_elements_by_class_name(element)
            if type.lower() == cons.LINK_TEXT.lower(): return self.driver.find_element_by_link_text(element)
        except Exception as e:
            print(f"{self.__class__.__name__}.{sys._getframe().f_code.co_name}:"
                  f"ERROR: {e}")
            return False

    def send_keyboard_key(self, key_value, **kwargs):
        for type, element in kwargs.items():
            if self.find_element_function(type, element):
                return self.find_element_function(type, element).send_keys(key_value)
            else:
                return False


if __name__ == "__main__":
    driver = Browser()
    driver.open_url(cons.PROJECT_PAGE)
