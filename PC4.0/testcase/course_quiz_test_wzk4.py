# coding=utf-8
import sys
from pages.course_model_quiz import CourseQuiz
from models import myunit


class CourseQuizTest(myunit.MyTest):
    u"""4.0PC模板课程-考试测验-创建"""
    sys.setrecursionlimit(150000)
    # upload_time = 100  # 文件上传默认等待最长时间，文件过大时需增大
    # file_url = 'D:\\test_input.txt'
    # file_url2 = 'D:\\50m.pdf'
    # coured_id = 'feac75aa-537b-3cb6-99c4-3e269747d262'
    # random.sample('zyxwvutsrqponmlkjihgfedcba', 30)

    def test0001_create_sucess001(self):
        u"""4.0PC模板课程-考试测验-创建成功："""
        create = CourseQuiz(self.driver)
        create.login()  # 登录
        create.enter_course_quiz_page()  # 进入模板课程-考试测验页面
        create.create_quiz()  # 新建考试测验

    def test0001_create_sucess002(self):
        u"""4.0PC模板课程-考试测验-创建成功："""
        create = CourseQuiz(self.driver)
        create.login()
        create.enter_course_quiz_page()
        create.create_quiz()

    def test0002_create_fail001(self):
        u"""4.0PC模板课程-考试测验-创建失败：测试名称 不能为空"""
        alert_info = "测试名称 不能为空"
        create = CourseQuiz(self.driver)
        create.login()
        create.enter_course_quiz_page()
        create.create_quiz(quiz_title='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail002(self):
        u"""4.0PC模板课程-考试测验-创建失败：测试名称 不能超过30个字符"""
        alert_info = "测试名称 不能超过30个字符"
        create = CourseQuiz(self.driver)
        create.login()
        create.enter_course_quiz_page()
        create.create_quiz(quiz_title='quiz_titlequiz_title')
        self.assertIn(alert_info, create.create_errors_info())

    def test0003_create_fail001(self):
        u"""4.0PC模板课程-考试测验-创建失败：试卷名称 不能为空："""
        alert_info = "试卷名称 不能为空"
        create = CourseQuiz(self.driver)
        create.login()
        create.enter_course_quiz_page()
        create.create_quiz(paper_title='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0003_create_fail002(self):
        u"""4.0PC模板课程-考试测验-创建失败：试卷名称 不能超过30个字符："""
        alert_info = "试卷名称 不能超过30个字符"
        create = CourseQuiz(self.driver)
        create.login()
        create.enter_course_quiz_page()
        create.create_quiz(paper_title='paper_titlepaper_title')
        self.assertIn(alert_info, create.create_errors_info())
