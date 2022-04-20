# coding=utf-8
import time
from selenium.webdriver.common.by import By
from pages.login_page import Loginpage


class CourseKnowledge(Loginpage):
    """------------以下为模板课程-知识点------------------"""
    course_Knowledge_url = "/index.php/LearningCenter/knowledge/index?course_id="

    def enter_course_knowledge_page(self, coured_id='feac75aa-537b-3cb6-99c4-3e269747d262'):
        """进入模板课程-知识点页面"""
        self.driver.get(self.base_url + self.course_Knowledge_url + self.bcourse_id)

    Knowledge_title_loc = (By.XPATH, '//input[@id="knowledgeform-knowledge"]')  # 知识点标题

    def entry_knowledge_detail(self, knowledge_title='Knowledge_title'):
        """输入知识点标题、内容等"""
        if knowledge_title:
            knowledge_title = knowledge_title + time.strftime("%Y-%m-%d %H-%M-%S")
            self.wait_for(lambda: self.driver.find_element(*self.Knowledge_title_loc)).send_keys(knowledge_title)

    def create_knowledge(self, knowledge_title='knowledge_title'):
        """创建知识点"""
        self.button_click(tap_text='a', button_text='新建')
        self.entry_knowledge_detail(knowledge_title=knowledge_title)
        self.button_click(tap_text='button', button_text='保存')

    Knowledge_errors_loc = (By.XPATH, '//div[@class="help-block"]')
    # 错误提示:知识点不能为空；不能超过30字符；该知识点已存在
    # 失败验证

    def create_errors_info(self):
        return self.errors_info(self.Knowledge_errors_loc)


if __name__ == "_main_":
    pass
