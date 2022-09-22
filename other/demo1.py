# coding: utf-8
#
import uiautomator2 as u2
import time
import logging
import re
import json
from selenium import webdriver

d = u2.connect()

d.click_post_delay = 1.5#
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(funcName)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info(d)
# d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/notification_list"]/android.widget.FrameLayout[1]').click()

d.press("home")

d.app_start("com.ticauto.weather:id/weather_cover")
