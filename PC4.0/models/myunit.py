# coding=utf-8
import os
import time
import unittest
from selenium import webdriver
from time import sleep
from .driver import firefox_browser, firefox_browser_no_display, chrome_browser, chrome_browser_no_display


class MyTest(unittest.TestCase):

    def setUp(self):
        # self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        # self.driver = webdriver.PhantomJS()
        self.driver = chrome_browser()
        # self.driver = chrome_browser_no_display()
        # self.driver = firefox_browser()
        # self.driver = firefox_browser_no_display()
        # self.driver.implicitly_wait(10)
        # self.driver.set_window_size(1920,1280)
        # self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        # self.driver.fullscreen_window()

    def tearDown(self):
        self.driver.quit()
