# coding=utf-8
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.login_page import Loginpage


class CourseQuestion(Loginpage):
    """---------------------------------以下为模板课程-题库--------------------------------------------"""
    course_question_part_url = '/LearningCenter/questionbank/question-bank?course_id='  # 模板课程-题库链接地址，course_id需传入

    def enter_course_question_page(self, coured_id='feac75aa-537b-3cb6-99c4-3e269747d262'):
        """进入模板课程-题库页面"""
        self.driver.get(self.base_url + self.course_question_part_url + self.bcourse_id)

    question_types_loc = (By.XPATH, '//a[contains(@href,"create-question")]')  # 习题类型

    def question_types_select(self, question_type='简答题'):
        # 选择习题类型并点击
        question_type_select = False
        question_types = self.driver.find_elements(*self.question_types_loc)
        for q_type in question_types:
            if q_type.get_attribute('text') == question_type:
                q_type.click()
                question_type_select = True
                break
        if question_type_select is False:
            print('题型错误，只能是"简答题、论述题、计算题、单选题、多选题、真假题、填空题"中的一种')
        return question_type

    question_knowledge_loc = (By.XPATH, "//ul[@class='select2-selection__rendered']")  # 选择知识点

    def question_knowledge_select(self, knowledge='knowledge'):
        """选择知识点"""
        if knowledge:
            self.knowledge_select(self.question_knowledge_loc)
        else:
            print("知识点不能为空")

    # 获取题干答案解析等iframe
    frame_body = (By.TAG_NAME, "body")  # frame主体输入框
    frames_loc = (By.XPATH, "//div[contains(@style,'hidden')]//iframe[not(@id='')]")  # 非选择题frame

    def get_iframes(self):
        # 获取frame：题干（第一个），答案（中间的）、解析（最后一个）
        self.wait_for(lambda: self.driver.find_element(*self.frames_loc))
        frames = self.driver.find_elements(*self.frames_loc)
        return frames

    choice_frames_loc = (By.XPATH, "//div[@id='choiceAnswer']//iframe")  # 非选择题frame

    def get_choice_iframes(self):
        # 获取选择题选项frame
        self.wait_for(lambda: self.driver.find_element(*self.choice_frames_loc))
        frames = self.driver.find_elements(*self.choice_frames_loc)
        return frames

    def write_frame_body_text(self, frame='frame', text='text'):
        # 输入内容-公用
        self.driver.switch_to.frame(frame)  # 切换至frame
        self.wait_for(lambda: self.driver.find_element(*self.frame_body)).send_keys(text)
        self.driver.switch_to.default_content()  # 切换出frame

    add_choice_button_loc1 = (By.XPATH, "//a[text()='增加答案']")  # 单选题多选题增加答案
    add_choice_button_loc = (By.XPATH, "//a[contains(@id,'add_')]")  # 单选题多选题增加答案

    def add_choice(self, times=4):
        """增加选项"""
        if times > 4:
            times = 4
        while times > 0:
            add_button = self.wait_for(lambda: self.driver.find_element(*self.add_choice_button_loc))
            actions = ActionChains(self.driver)
            actions.move_to_element(add_button)
            add_button.click()
            times = times - 1

    choices_loc = (By.XPATH, "//input[contains(@class,'_check')]")

    def click_choice(self, question_type='单选题'):
        choices = self.driver.find_elements(*self.choices_loc)
        if question_type == '单选题' or question_type == '单选':
            choices[0].click()
        if question_type == '多选题' or question_type == '多选':
            choices[0].click()
            choices[1].click()
        if question_type == '真假题' or question_type == '真假':
            choices[-1].click()
        else:
            pass

    def entry_question_detail(self, question_type='简答题', title='title', answer='答案', times=4, choice=True):
        # 输入习题内容
        if question_type == '单选题' or question_type == '多选题':
            self.add_choice(times=times)
        if question_type == '填空题' or question_type == '填空':
            self.add_choice(times=times)
        if choice:
            self.click_choice(question_type=question_type)
        frames = self.get_iframes()
        answer_frames = frames[1:-1]
        self.question_knowledge_select()  # 习题知识点
        if title:
            title = title + time.strftime("%Y-%m-%d %H-%M-%S") + '-' + frames[0].get_attribute('id')
            self.write_frame_body_text(frame=frames[0], text=title)  # 习题标题
        note = '解析' + time.strftime("%Y-%m-%d %H-%M-%S") + '-' + frames[-1].get_attribute('id')  # 解析文本
        self.write_frame_body_text(frame=frames[-1], text=note)  # 习题解析
        if answer:
            if question_type == '简答题' or question_type == '论述题' or question_type == '计算题':
                answer = answer + time.strftime("%Y-%m-%d %H-%M-%S") + '-' + answer_frames[0].get_attribute('id')  # 答案文本
                self.write_frame_body_text(frame=answer_frames[0], text=answer)  # 主观题习题答案
            if question_type == '单选题' or question_type == '多选题' or question_type == '填空题':
                for answer_frame in answer_frames:
                    answer = question_type + time.strftime("%Y-%m-%d %H-%M-%S") + '-' + answer_frame.get_attribute('id')
                    self.write_frame_body_text(frame=answer_frame, text=answer)  # 客观题习题答案

    def create_question(self, title='title', question_type='简答题', times=4, choice=True, answer='答案'):
        self.button_click(tap_text='button', button_text='新建')
        self.question_types_select(question_type=question_type)
        self.entry_question_detail(title=title, question_type=question_type, times=times, choice=choice, answer=answer)
        self.button_click(tap_text='button', button_text='保存')

    create_errors_loc = (By.XPATH, "//span[@class='error_message']")
    create_success_loc = (By.XPATH, "//p[contains(text(),'欢迎登录')]")
    # 错误提示:题干内容不能为空；习题答案不能为空；；知识点不能为空；
    # 请选择一项作为答案选项；答案选项内容不能重复；
    # 请至少选择两项作为答案选项；习题答案不能为空；
    # 请选择一项作为答案选项；
    # 请为题干添加填空；
    # 失败验证

    def create_errors_info(self):
        return self.errors_info(element=self.create_errors_loc)
