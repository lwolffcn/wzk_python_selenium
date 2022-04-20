from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os, time

driver = webdriver.Firefox()
file_path =  'file:///' + os.path.abspath('upfile.html')

driver.get(file_path)

# driver.find_element_by_name("file").send_keys('D:\\wzk_python_selenium\\PC4.0\\files\\upload_file.txt')
# # time.sleep(1)

# 单击打开上传窗口
# driver.find_element_by_name("file").click()
file_click = driver.find_element_by_name("file")
action = ActionChains(driver)
action.move_to_element(file_click).click().perform()
action.release()
time.sleep(1)
# 调用upfile.exe上传程序
os.system("D:\\wzk_python_selenium\\PC4.0\\files\\up.exe")
time.sleep(1)

driver.quit()