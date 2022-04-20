import os

from models.driver import firefox_browser



dr = firefox_browser()
dr.maximize_window()
dr.get('http://wzk.36ve.com')


print('hello!')


dr.quit()