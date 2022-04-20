# coding=utf-8
import time
from selenium.webdriver.common.by import By
from pages.login_page import Loginpage


class CourseTeacher(Loginpage):
    """------------以下为模板课程-教师------------------"""
    course_teacher_url = "/index.php/LearningCenter/teacherteam/index?course_id="

    def enter_course_teacherteam_page(self, coured_id='feac75aa-537b-3cb6-99c4-3e269747d262'):
        """进入模板课程-教师页面"""
        self.driver.get(self.base_url + self.course_teacher_url + self.bcourse_id)

    teacher_title_loc = (By.XPATH, '//input[@id="teacherform-teacher"]')  # 教师标题

    def entry_teacher_detail(self, teacher_title='teacher_title'):
        """输入教师标题、内容等"""
        if teacher_title:
            teacher_title = teacher_title + time.strftime("%Y-%m-%d %H-%M-%S")
            self.wait_for(lambda: self.driver.find_element(*self.teacher_title_loc)).send_keys(teacher_title)

    def create_teacher(self, teacher_title='teacher_title'):
        """创建教师"""
        self.button_click(tap_text='a', button_text='新建')
        self.entry_teacher_detail(teacher_title=teacher_title)
        self.button_click(tap_text='button', button_text='保存')

    teacher_errors_loc = (By.XPATH, '//div[@class="help-block"]')
    # 错误提示:教师不能为空；不能超过30字符；该教师已存在
    # 失败验证

    def create_errors_info(self):
        return self.errors_info(self.teacher_errors_loc)


if __name__ == "_main_":
    pass
