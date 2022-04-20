# coding=utf-8
import time
from selenium.webdriver.common.by import By
from pages.login_page import Loginpage


class CourseQuiz(Loginpage):
    """------------以下为模板课程-考试测验------------------"""
    course_quiz_url = "/index.php/LearningCenter/question/index?course_id="

    def enter_course_quiz_page(self, coured_id='feac75aa-537b-3cb6-99c4-3e269747d262'):

        """进入模板课程-考试测验页面"""
        self.driver.get(self.base_url + self.course_quiz_url + self.bcourse_id)

    quiz_title_loc = (By.XPATH, '//input[@id="addwebquizpaper-quiz_name"]')  # 考试测验-测验标题
    quiz_paper_title_loc = (By.XPATH, '//input[@id="addwebquizpaper-title"]')  # 考试测验-试卷标题

    def entry_quiz_detail(self, quiz_title='quiz_title', paper_title='paper_title'):
        """输入考试测验标题、内容等"""
        if quiz_title:
            quiz_title = quiz_title + time.strftime("%Y-%m-%d %H-%M-%S")
            self.wait_for(lambda: self.driver.find_element(*self.quiz_title_loc)).send_keys(quiz_title)
        if paper_title:
            paper_title = paper_title + time.strftime("%Y-%m-%d %H-%M-%S")
            self.wait_for(lambda: self.driver.find_element(*self.quiz_paper_title_loc)).send_keys(paper_title)

    def create_quiz(self, quiz_title='quiz_title', paper_title='paper_title'):
        """创建考试测验"""
        self.button_click(tap_text='a', button_text='新建')
        self.entry_quiz_detail(quiz_title=quiz_title, paper_title=paper_title)
        self.button_click(tap_text='button', button_text='保存')

    # 错误提示:测试名称 不能为空；试卷名称 不能为空；测试名称 不能超过30个字符;试卷名称 不能超过30个字符
    # 失败验证

    def create_errors_info(self):
        return self.errors_info()


if __name__ == "_main_":
    pass
