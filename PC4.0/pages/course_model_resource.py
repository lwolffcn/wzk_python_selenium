# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import Loginpage
import requests, time
import urllib.request

class CourseResource(Loginpage):
    """---------------------------------以下为模板课程-素材--------------------------------------------"""
    course_resource_url = "/LearningCenter/material/index?course_id="

    def enter_course_resource_page(self, course_id='feac75aa-537b-3cb6-99c4-3e269747d262'):
        """进入模板课程-素材页面"""
        self.driver.get(self.base_url + self.course_resource_url + self.bcourse_id)

    create_resource_button_loc1 = (By.XPATH, "//a[contains(@href,'add-resource')]")
    resource_knowledge_loc = (By.XPATH, "//input[@class='select2-search__field']")  # 知识点

    def resource_knowledge_select(self, knowledge='knowledge'):
        """选择知识点"""
        self.knowledge_select(self.resource_knowledge_loc)

    resource_apply_type_loc = (By.XPATH, "//select[contains(@id,'apply')]")  # 应用类型
    resource_mime_type_loc = (By.XPATH, "//select[@id='addresourceform-mimetype']")  # 媒体类型
    resource_language_loc = (By.XPATH, "//select[@id='addresourceform-mat_lang']")  # 语言类型
    resource_group_id_loc = (By.XPATH, "//select[@id='addresourceform-group_id']")  # 组id

    def resource_apply_type_select(self, type_text='专业标准'):
        # 选择素材应用类型
        resource_apply = self.wait_for(lambda: self.driver.find_element(*self.resource_apply_type_loc))
        self.select_choice(resource_apply, type_text=type_text)

    def resource_mime_type_select(self, type_text='其他'):
        # 选择素材媒体类型
        resource_mime_type = self.wait_for(lambda: self.driver.find_element(*self.resource_mime_type_loc))
        self.select_choice(resource_mime_type, type_text=type_text)

    def resource_lang_type_select(self, type_text='中文'):
        resource_language = self.wait_for(lambda: self.driver.find_element(*self.resource_language_loc))
        # 选择素材语言类型
        self.select_choice(resource_language, type_text=type_text)

    def resource_group_id_select(self, type_text='默认组'):
        resource_group_id = self.wait_for(lambda: self.driver.find_element(*self.resource_group_id_loc))
        # 选择素材组id
        self.select_choice(resource_group_id, type_text=type_text)

    # 处理上传文件
    resource_name_loc = (By.XPATH, "//input[@id='addresourceform-file_title']")  # 素材名称
    resource_form_id = 'add-resource-form'

    def entry_resource_detail(self, knowledge='knowledge', apply_type='专业标准', mime_type='PPT演示文稿', language='中文',
                              group_id='默认组', name='name', upload_time=10, file_urls='',):
        """模板课程-创建素材"""
        if knowledge:
            self.resource_knowledge_select(knowledge=knowledge)  # 选择知识点
        if apply_type:
            self.resource_apply_type_select(type_text=apply_type)  # 选择应用类型
        if mime_type:
            self.resource_mime_type_select(type_text=mime_type)  # 选择媒体类型
        if language:
            self.resource_lang_type_select(type_text=language)  # 选择语言类型
        if group_id:
            self.resource_group_id_select(type_text=group_id)  # 选择组
        if name:
            name = name + '-' + mime_type
            self.wait_for(lambda: self.driver.find_element(*self.resource_name_loc)).send_keys(name)
        if self.upload_files(file_urls=file_urls, upload_time=upload_time,):
            self.button_click(tap_text='button', button_text='保存')
        else:
            print('文件未上传完毕！')

    def create_resource(self, knowledge='knowledge', apply_type='专业标准', mime_type='PPT演示文稿', language='中文',
                        group_id='默认组', name='name', upload_time=10, file_urls=''):
        self.button_click(tap_text='a', button_text='新建')  # 点击新建素材按钮
        self.entry_resource_detail(knowledge=knowledge, apply_type=apply_type, mime_type=mime_type, language=language,
                                   group_id=group_id, name=name, upload_time=upload_time, file_urls=file_urls)

    batch_file_url_loc = (By.XPATH, "//input[@id='w0']")  # 实际上传的文件路径
    batch_apply_type_loc = (By.XPATH, "//select[contains(@id,'_applyType')]")  # 应用类型

    def batch_resource_apply_type_select(self, type_text='专业标准'):
        """批量选择素材应用类型"""
        self.wait_for(lambda: self.driver.find_element(*self.resource_apply_type_loc))
        resource_apply_types = self.wait_for(lambda: self.driver.find_elements(*self.resource_apply_type_loc))
        for resource_apply_type in resource_apply_types:
            self.select_choice(resource_apply_type, type_text=type_text)

    def batch_create_resource(self, file_lists='', knowledge='knowledge', type_text='专业标准',
                              language='中文', group_id='默认组', name='name', upload_time=10,):
        self.button_click(tap_text='a', button_text='批量上传')
        self.upload_files(file_urls=file_lists, upload_time=upload_time)
        self.button_click(tap_text='button', button_text='下一步')
        self.resource_knowledge_select(knowledge=knowledge)
        self.batch_resource_apply_type_select(type_text=type_text)
        self.button_click(tap_text='button', button_text='保存')

    create_success_loc = (By.XPATH, "//p[contains(text(),'欢迎登录')]")
    # 错误提示:素材不能为空，请上传素材;知识点不能为空;应用类型不能为空;媒体类型不能为空;语言类型不能为空
    # 不正确的文件扩展名 "Script.jmx". 只支持 "jpg, png, jpeg, gif, pdf, mp4, doc, docx, xls, xlsx, ppt, pptx, mp3, txt, html, flv, swf, avi, zip, rar" 的文件扩展名.
    # 文件 "appScan.rar" (1157828.95 KB) 超过了允许大小 512000 KB.
    # 失败验证

    def create_errors_info(self):
        return self.errors_info()


class DelResource(Loginpage):
    m_url = '/index.php/ManageCenter/resource/manage-resource-list'  # 模板课程-题库链接地址，course_id需传入
    dels_loc = (By.XPATH, "//a[text()='删除']")

    @staticmethod
    def html_test():
        """进入模板课程-题库页面"""
        # requests.DEFAULT_RETRIES = 5  # 增加重连次数
        # s = requests.session()
        # s.keep_alive = False  # 关闭多余连接
        # responses = s.get(r'http://wzk.36ve.com/index.php/ManageCenter/resource/manage-resource-list')  # 你需要的网址
        # time.sleep(1)
        # htmls = responses.content.decode('utf8')
        # print(htmls)

        request = urllib.request.Request(r'http://wzk.36ve.com/index.php/ManageCenter/resource/manage-resource-list')
        response = urllib.request.urlopen(request)
        htmls = response.read()
        print(htmls)

        # response = requests.get(self.base_url + self.m_url)
        # html = response.content.decode('utf8')
        # print(html)

    def enter_course_question_page(self):
        """进入模板课程-题库页面"""
        self.driver.get(self.base_url + self.m_url)

    def click_delete_button(self, dels):
        self.wait_for(lambda: dels.is_enabled())
        dels.click()
        # if dels.is_enabled():
        #     dels.click()
        # self.button_click(tap_text='a', button_text='删除')

    def click_ok(self):
        WebDriverWait(self.driver, 20).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # print(alert.text)
        alert.accept()

    def click_okok(self):
        alert = self.wait_for(self.driver.switch_to.alert)
        alert.accept()
        # if '确定删除' in alert.text:
        #     alert.accept()

    def del_while(self):
        dels = self.wait_for_del_buttons()
        # print(len(dels))
        while len(dels):
            self.click_delete_button(dels[-1])
            self.click_ok()
            self.driver.refresh()
            self.del_while()

    def del_all(self):
        # dels = self.wait_for_del_buttons()
        dela = self.wait_for(lambda: self.driver.find_element(By.XPATH, "//a[text()='删除']"))
        dels = self.wait_for(lambda: self.driver.find_elements(By.XPATH, "//a[text()='删除']"))
        print(len(dels))
        while len(dels):
            self.click_delete_button(dels[0])
            self.click_okok()
            self.driver.refresh()
            self.del_all()


if __name__ == "_main_":
    pass
