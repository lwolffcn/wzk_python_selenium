# coding=utf-8
import sys
sys.path.append('D:\\wzk_python_selenium\\PC4.0')
from pages.course_model import CourseModel
from models import myunit


class CourseModelTest(myunit.MyTest):
    u"""4.0PC模板课程-创建"""
    # sys.setrecursionlimit(150000)

    def test0001_create_sucess001(self):
        u"""4.0PC模板课程-创建成功：标准化课程"""
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(course_type='标准化课程')
        
    def test0001_create_sucess002(self):
        u"""4.0PC模板课程-创建成功：个性化课程"""
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(course_type='个性化课程')

    def test0001_create_sucess003(self):
        u"""4.0PC模板课程-创建成功：创新课程"""
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(course_type='创新课程')

    def test0002_create_fail001(self):
        u"""4.0PC模板课程-创建失败：课程名称不能为空"""
        alert_info = "课程名称不能为空"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(name='', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())

    def test0002_create_fail002(self):
        u"""4.0PC模板课程-创建失败：课程名称不能超过60个字符"""
        alert_info = "课程名称不能超过60个字符"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(name='namenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamename', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())

    def test0003_create_fail001(self):
        u"""4.0PC模板课程-创建失败：关键字不能为空"""
        alert_info = "关键字不能为空"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(keyword='', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())

    def test0003_create_fail002(self):
        u"""4.0PC模板课程-创建失败：关键字不能超过60个字符"""
        alert_info = "关键字不能超过60个字符"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(keyword='keywordkeywordkeywordkeywordkeywordkeywordkeywordkeywordkeywordkeyword', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())

    def test0004_create_fail001(self):
        u"""4.0PC模板课程-创建失败：总学时不能为空"""
        alert_info = "总学时不能为空"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(total_hours='', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())

    def test0004_create_fail002(self):
        u"""4.0PC模板课程-创建失败：总学时必须为大于0的整数"""
        alert_info = "总学时必须为大于0的整数"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(total_hours='hh', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())

    def test0004_create_fail003(self):
        u"""4.0PC模板课程-创建失败：总学时必须为小于等于200的整数"""
        alert_info = "总学时必须为小于等于200的整数"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(total_hours='10000', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())

    def test0005_create_fail004(self):
        u"""4.0PC模板课程-创建失败：课程简介不能为空"""
        alert_info = "课程简介不能为空"
        create = CourseModel(self.driver)
        create.login()
        create.enter_couser_model_page()  # 进入模板课程管理页面
        create.create_course_model(summary='', course_type='标准化课程')
        self.assertEqual(alert_info, create.create_errors_info())
