import os

from selenium import webdriver


def FirefoxBrowser():
    driver= webdriver.Firefox()
    return driver

def ChromeBrowser():
    driver= webdriver.Chrome()
    return driver

"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from models import myunit,function


zyk_login_username_loc = (By.CSS_SELECTOR,'input#edit-name')
try:
            self.driver.find_element(*self.zyk_login_password_loc)
        except NoSuchElementException as e:
            print(e)
"""


#dr = FirefoxBrowser()
print('hello BasePage!')

if __name__ == "_main_":
    pass