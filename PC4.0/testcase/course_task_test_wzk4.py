# coding=utf-8
import sys
from pages.course_model_task import CourseTask
from models import myunit


class CourseTaskTest(myunit.MyTest):
    u"""4.0PC模板课程-实训任务-创建"""
    sys.setrecursionlimit(150000)
    # upload_time = 100  # 文件上传默认等待最长时间，文件过大时需增大
    # file_url = 'D:\\test_input.txt'
    # file_url2 = 'D:\\50m.pdf'
    # coured_id = 'feac75aa-537b-3cb6-99c4-3e269747d262'

    def test0001_create_sucess001(self):
        u"""4.0PC模板课程-实训任务-不启用分组任务创建成功："""
        create = CourseTask(self.driver)
        create.login()
        create.enter_course_task_page()
        create.create_task(type_select='不启用分组')

    def test0001_create_sucess002(self):
        u"""4.0PC模板课程-实训任务-启用分组任务创建成功："""
        create = CourseTask(self.driver)
        create.login()
        create.enter_course_task_page()
        create.create_task(type_select='启用分组')

    def test0002_create_fail001(self):
        u"""4.0PC模板课程-实训任务-创建失败：任务标题不能为空"""
        alert_info = "任务标题不能为空"
        create = CourseTask(self.driver)
        create.login()
        create.enter_course_task_page()
        create.create_task(title='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail002(self):
        u"""4.0PC模板课程-实训任务-创建失败：任务目标不能为空："""
        alert_info = "任务目标不能为空"
        create = CourseTask(self.driver)
        create.login()
        create.enter_course_task_page()
        create.create_task(goal='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail003(self):
        u"""4.0PC模板课程-实训任务-创建失败：任务内容不能为空："""
        alert_info = "任务内容不能为空"
        create = CourseTask(self.driver)
        create.login()
        create.enter_course_task_page()
        create.create_task(content='')
        self.assertIn(alert_info, create.create_errors_info())
