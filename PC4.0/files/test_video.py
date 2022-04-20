from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import logging


logging.basicConfig(level=logging.DEBUG)


driver = webdriver.Firefox()
driver.get ("https://videojs.com/")
video = driver.find_element_by_xpath("//*[@id='vjs_video_3_html5_api']")
# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print (url)
# 播放视频
print("start")
action = ActionChains(driver)
# action.move_to_element(video).click().perform()
action.click(video).perform()
# video.click()
# driver.execute_script("return arguments[0].play()", video)
#播放15秒钟
sleep(15)
#暂停视频
print("stop")
driver.execute_script("arguments[0].pause()", video)
sleep(1)

# 获取视频文件的时长
print("获取视频文件的时长")
print(driver.execute_script("return arguments[0].duration", video))
sleep(3)

driver.quit()