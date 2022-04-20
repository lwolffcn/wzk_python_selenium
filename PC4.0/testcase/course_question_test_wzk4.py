# coding=utf-8
import sys
from pages.course_model_question import CourseQuestion
from models import myunit, function


class CourseQuestionTest(myunit.MyTest):
    u"""4.0PC模板课程-习题-创建"""
    sys.setrecursionlimit(150000)
    # upload_time = 100  # 文件上传默认等待最长时间，文件过大时需增大
    # file_url = 'D:\\test_input.txt'
    # file_url2 = 'D:\\50m.pdf'
    # coured_id = 'feac75aa-537b-3cb6-99c4-3e269747d262'

    def test0001_create_sucess001(self):
        u"""4.0PC模板课程-习题-简答题-创建成功："""
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='简答题', question_type='简答题')

    def test0001_create_sucess002(self):
        u"""4.0PC模板课程-习题-论述题-创建成功："""
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='论述题', question_type='论述题')

    def test0001_create_sucess003(self):
        u"""4.0PC模板课程-习题-计算题-创建成功："""
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='计算题', question_type='计算题')

    def test0001_create_sucess004(self):
        u"""4.0PC模板课程-习题-单选题-创建成功："""
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='单选题', question_type='单选题')

    def test0001_create_sucess005(self):
        u"""4.0PC模板课程-习题-多选题-创建成功："""
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='多选题', question_type='多选题')

    def test0001_create_sucess006(self):
        u"""4.0PC模板课程-习题-真假题-创建成功："""
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='真假题', question_type='真假题')

    def test0001_create_sucess007(self):
        u"""4.0PC模板课程-习题-填空题-创建成功："""
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='填空题', question_type='填空题')

    def test0002_create_fail001(self):
        u"""4.0PC模板课程-习题-创建失败：题干内容不能为空"""
        alert_info = "题干内容不能为空"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='', question_type='简答题')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail002(self):
        u"""4.0PC模板课程-习题-创建失败-主观题：习题答案不能为空："""
        alert_info = "习题答案不能为空"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(answer='', question_type='简答题')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail003(self):
        u"""4.0PC模板课程-习题-创建失败-多选题：习题答案不能为空："""
        alert_info = "习题答案不能为空"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(answer='', question_type='多选题')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail004(self):
        u"""4.0PC模板课程-习题-创建失败-单选题：习题答案不能为空："""
        alert_info = "习题答案不能为空"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(answer='', question_type='单选题')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail005(self):
        u"""4.0PC模板课程-习题-创建失败-单选题：请选择一项作为答案选项："""
        alert_info = "请选择一项作为答案选项"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(question_type='单选题', choice='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail006(self):
        u"""4.0PC模板课程-习题-创建失败-多选题：请至少选择两项作为答案选项："""
        alert_info = "请至少选择两项作为答案选项"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(question_type='多选题', choice='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail007(self):
        u"""4.0PC模板课程-习题-创建失败-真假题：请选择一项作为答案选项："""
        alert_info = "请选择一项作为答案选项"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(question_type='真假题', choice='')
        self.assertIn(alert_info, create.create_errors_info())

    def test0002_create_fail008(self):
        u"""4.0PC模板课程-习题-创建失败-填空题：请为题干添加填空："""
        alert_info = "请为题干添加填空"
        create = CourseQuestion(self.driver)
        create.login()
        create.enter_course_question_page()
        create.create_question(title='填空题', question_type='填空题', times=0)
        self.assertIn(alert_info, create.create_errors_info())
