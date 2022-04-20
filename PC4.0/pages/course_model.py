# coding=utf-8
import time
from selenium.webdriver.common.by import By
from pages.login_page import Loginpage


class CourseModel(Loginpage):
    # web_url = "http://wzk.36ve.com"  # 网址首页页面url
    # login_url = "http://wzk.36ve.com/login/login"  # 登录页面url
    course_model_url = "/index.php/course/organize-course"  # 模板课程管理页面url

    def enter_couser_model_page(self):
        # 进入模板课程管理页面
        self.driver.get(self.base_url+self.course_model_url)

    alert_windows = (By.XPATH, "//div/a[@id='createCOurse']//div[@class='modal-content']")

    def swtich_to_to(self):
        # 获取当前窗口所有句柄
        all_windows = self.driver.window_handles
        # 获取当前标签页窗口句柄
        current_window = self.driver.current_window_handle
        for window in all_windows:
            if window != current_window:
                print("切换前的窗口名称是：", self.driver.title)
                self.driver.switch_to_window(window)
                time.sleep(2)
                print("切换后的窗口名称是：", self.driver.title)
                break
            else:
                print('未切换窗口')

    course_model_name_loc = (By.XPATH, "//input[@id='addcourseform-coursename']")  # 模板课程名称addcourseform-coursename
    course_model_keyword_loc = (By.XPATH, "//input[@id='addcourseform-coursekeyword']")  # 模板课程关键字
    course_model_type_loc = (By.XPATH, "//select[@id='addcourseform-coursetype']")  # 模板课程类型
    course_model_language_loc = (By.XPATH, "//label/input[@name='AddCourseForm[course_lang]']")  # 模板课程语言类型
    course_model_language_loc2 = (By.XPATH, "//label/input[@value='courseLanguage.english']")  # 模板课程语言类型
    course_model_group_id_loc = (By.XPATH, "//select[@id='addcourseform-group_id']")  # 模板课程所属组
    group_id_loc = (By.XPATH, "//option[@value='65f00449-78c4-39f5-83c7-0f3707e8b009']")
    course_model_total_hours_loc = (By.XPATH, "//input[@id='addcourseform-totalhours']")  # 模板课程总学时
    course_model_summary_loc = (By.XPATH, "//textarea[@id='addcourseform-coursedescription']")  # 模板课程简介
    course_model_save_button_loc = (By.XPATH, "//button[text()='保存']")  # 模板课程保存按钮

    def course_model_type_select(self, type_text='标准化课程'):
        # 选择课程类型
        model_type = self.wait_for(lambda: self.driver.find_element(*self.course_model_type_loc))
        self.select_choice(model_type, type_text=type_text)

    def entry_course_model(self, name='name', keyword='keyword', course_type='标准化课程', language='courseLanguage.english',
                                   group_id='65f00449-78c4-39f5-83c7-0f3707e8b009', total_hours='100', summary='summary'):
        """输入内容并创建模板课程"""
        if name:
            name = name + time.strftime("%Y-%m-%d %H-%M-%S")
        self.wait_for(lambda: self.driver.find_element(*self.course_model_name_loc)).send_keys(name)
        self.wait_for(lambda: self.driver.find_element(*self.course_model_keyword_loc)).send_keys(keyword)
        self.course_model_type_select(course_type)  # 选择课程类型
        self.wait_for(lambda: self.driver.find_element(*self.course_model_total_hours_loc)).send_keys(total_hours)
        self.wait_for(lambda: self.driver.find_element(*self.course_model_summary_loc)).send_keys(summary)
        return name

    def create_course_model(self, name='name', keyword='keyword', course_type='标准化课程', language='courseLanguage.english',
                            group_id='65f00449-78c4-39f5-83c7-0f3707e8b009', total_hours='100', summary='summary'):
        """创建模板课程"""
        self.button_click(tap_text='a', button_text='创建课程模板')  # 打开创建模板课程窗口
        self.entry_course_model(name=name, keyword=keyword, course_type=course_type, language=language,
                                        group_id=group_id, total_hours=total_hours, summary=summary)  # 输入内容并创建模板课程
        self.button_click(tap_text='button', button_text='保存')

    create_success_loc = (By.XPATH, "//p[contains(text(),'欢迎登录')]")
    # 错误提示:课程名称不能为空、课程名称不能超过60个字符等
    # 失败验证

    def create_errors_info(self):
        return self.errors_info()


if __name__ == "_main_":
    pass
