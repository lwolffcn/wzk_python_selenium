# coding=utf-8
import sys
from pages.course_model_knowledge import CourseKnowledge
from models import myunit



class CourseKnowledgeTest(myunit.MyTest):
    u"""4.0PC模板课程-知识点-创建"""
    sys.setrecursionlimit(150000)
    upload_time = 100  # 文件上传默认等待最长时间，文件过大时需增大
    file_url = 'D:\\test_input.txt'  # 文件路径

    def test0001_create_sucess001(self):
        u"""4.0PC模板课程-知识点-创建成功"""
        create = CourseKnowledge(self.driver)
        create.login()
        create.enter_course_knowledge_page()
        create.create_knowledge(knowledge_title='专业标准')

    def test0001_create_sucess002(self):
        u"""4.0PC模板课程-知识点-创建成功"""
        create = CourseKnowledge(self.driver)
        create.login()
        create.enter_course_knowledge_page()
        create.create_knowledge(knowledge_title='专业标准2')

    def test0002_create_fail001(self):
        u"""4.0PC模板课程-知识点-创建失败：知识点不能为空"""
        alert_info = "知识点不能为空"
        create = CourseKnowledge(self.driver)
        create.login()
        create.enter_course_knowledge_page()
        create.create_knowledge(knowledge_title='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail002(self):
        u"""4.0PC模板课程-知识点-创建失败：不能超过30字符"""
        alert_info = "不能超过30字符"
        create = CourseKnowledge(self.driver)
        create.login()
        create.enter_course_knowledge_page()
        create.create_knowledge(knowledge_title='不能超过30字符不能超过30字符不能超过30字符不能超过30字符不能超过30字符')
        self.assertIn(alert_info, create.create_errors_info())
