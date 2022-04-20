# coding=utf-8
import time
from selenium.webdriver.common.by import By
from pages.login_page import Loginpage


class CourseTask(Loginpage):
    """---------------------------------以下为模板课程-实训任务--------------------------------------------"""
    course_task_url = '/index.php/LearningCenter/simulationtasks/index?course_id='

    def enter_course_task_page(self, coured_id='feac75aa-537b-3cb6-99c4-3e269747d262'):
        """进入模板课程-实训任务页面"""
        self.driver.get(self.base_url + self.course_task_url + self.bcourse_id)

    has_gprou_loc = (By.XPATH, '//select[@id="tcoursetask-user_task_group"]')  # 是否启用分组

    def has_group(self, type_text='不启用分组'):
        """是否启用分组"""
        has_gprou = self.wait_for(lambda: self.driver.find_element(*self.has_gprou_loc))
        self.select_choice(has_gprou, type_text=type_text)

    son_task_title_loc = (By.XPATH, '//input[contains(@name,"son_task_title")]')  # 子任务标题
    son_task_content_loc = (By.XPATH, '//textarea[contains(@name,"son_task_content")]')  # 子任务内容
    add_son_task_button_loc = (By.XPATH, '//a[@id="add_son_task"]')

    def entry_son_task_detail(self, title='title', content='content'):
        """输入子任务标题及内容"""
        self.wait_for(lambda: self.driver.find_element(*self.son_task_title_loc))
        sons_task_title = self.driver.find_elements(*self.son_task_title_loc)
        self.wait_for(lambda: self.driver.find_element(*self.son_task_content_loc))
        sons_task_content = self.driver.find_elements(*self.son_task_content_loc)
        if title:
            for son in sons_task_title:
                son.send_keys(title + '-' + son.get_attribute('name'))
        if content:
            for son in sons_task_content:
                son.send_keys(content + time.strftime("%Y-%m-%d %H-%M-%S") + '-' + son.get_attribute('name'))

    task_title_loc = (By.XPATH, '//input[@id="tcoursetask-task_title"]')  # 实训任务标题
    task_goal_loc = (By.XPATH, '//input[@id="tcoursetask-task_goal"]')  # 实训任务目标
    task_content_loc = (By.XPATH, '//textarea[@id="tcoursetask-task_content"]')  # 实训任务内容

    def entry_task_detail(self, title='title', goal='goal', content='content', type_select='不启用分组'):
        """输入任务标题、目标、内容等"""
        if title:
            title = title + time.strftime("%Y-%m-%d %H-%M-%S")
            self.wait_for(lambda: self.driver.find_element(*self.task_title_loc)).send_keys(title)
        if goal:
            goal = goal + time.strftime("%Y-%m-%d %H-%M-%S")
            self.wait_for(lambda: self.driver.find_element(*self.task_goal_loc)).send_keys(goal)
        if content:
            content = content + time.strftime("%Y-%m-%d %H-%M-%S")
            self.wait_for(lambda: self.driver.find_element(*self.task_content_loc)).send_keys(content)
        if type_select == '启用分组':
            self.has_group(type_select)
            self.entry_son_task_detail()

    def create_task(self, title='title', goal='goal', content='content', type_select='不启用分组'):
        """创建实训任务"""
        self.button_click(tap_text='a', button_text='新建')  # 点击新建实训任务按钮
        self.entry_task_detail(title=title, goal=goal, content=content, type_select=type_select)
        self.button_click(tap_text='button', button_text='确定')  # 点击保存实训任务按钮

    # 错误提示:任务标题不能为空；任务目标不能为空；；任务内容不能为空；任务标题不能超过100字符;任务目标不能超过100字符
    # 失败验证

    def create_errors_info(self):
        return self.errors_info()


if __name__ == "_main_":
    pass
