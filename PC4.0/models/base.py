# coding=utf-8
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

MAX_WAIT = 10


class Base:
    """基础类"""
    base_url = "http://wzk.36ve.com"
    url = ''
    bcourse_id = 'feac75aa-537b-3cb6-99c4-3e269747d262'  # 模板课程id

    def __init__(self, selenium_driver, base_url=base_url, bcourse_id=bcourse_id, parent=None):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        self.base_url = base_url
        self.driver = selenium_driver
        self.bcourse_id = bcourse_id
        self.parent = parent

    def _open(self, url):
        # print("打开url....")
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), "Did not load on %s" % url

    def find(self, *loc):
        return self.driver.find_element(*loc)

    def finds(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def wait_for_del_buttons(self):
        start_time = time.time()
        while True:
            try:
                self.driver.find_element(By.XPATH, "//a[text()='删除']")
                del_buttons = self.driver.find_elements(By.XPATH, "//a[text()='删除']")
                return del_buttons
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
            time.sleep(0.5)

    def wait_for(self, fn, wait_time=MAX_WAIT):
        start_time = time.time()
        while True:
            try:
                if callable(fn):
                    return fn()
                else:
                    return fn
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > wait_time:
                    raise e
            time.sleep(0.5)

    def knowledge_select(self, element_loc):
        self.wait_for(self.driver.find_element(*element_loc))
        knowledge_selects = self.wait_for(self.driver.find_elements(*element_loc))
        for k in knowledge_selects:
            k.click()
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def select_choice(self, element, type_text=''):
        # 处理select选择框
        type_text_list = []
        for select_type in Select(element).options:
            # print(type.text)
            type_text_list.append(select_type.text)
        if type_text in type_text_list:
            Select(element).select_by_visible_text(type_text)
        else:
            print("类型不能为空")

    def upload_files(self, file_upload_success_loc='', file_urls='', upload_time=10):
        file_url_loc = (By.XPATH, "//input[@id='w0']")
        file_upload_success_loc = (By.XPATH, "//div[@class='kv-upload-progress kv-hidden']/div/div[contains(text(),'完成')]")
        upload_success = False
        files_upload = self.wait_for(lambda: self.driver.find_element(*file_url_loc))
        for file_url in file_urls:
            files_upload.send_keys(file_url)
        self.button_click(tap_text='span', button_text='上传')
        try:
            self.wait_for(lambda: self.driver.find_element(*file_upload_success_loc), wait_time=upload_time)
            upload_success = True
        except TimeoutException:
            print('文件未上传完毕')
        finally:
            return upload_success

    def button_click(self, tap_text='button', button_text='保存'):
        """点击新建、保存、下一步等按钮"""
        self.wait_for(lambda: self.driver.find_element(By.XPATH, "//%s[text()='%s']" % (tap_text, button_text))).click()
        sleep(1)

    errors_loc = (By.XPATH, "//p[contains(@class,'help-block-error')]")

    def errors_info(self, element=errors_loc):
        """失败提示"""
        self.wait_for(lambda: self.driver.find_element(*element))
        errors_info = self.driver.find_elements(*element)
        errors_str = ''
        for error in errors_info:
            errors_str = errors_str + error.text
        print('失败：%s' % errors_str)
        return errors_str

    def form_submit_by_id(self, form_id=''):
        """submit form"""
        self.driver.find_element(By.XPATH, "//form[@id='%s']" % form_id).submit()
        sleep(1)
