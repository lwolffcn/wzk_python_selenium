# coding=utf-8
import sys
from pages.course_model_resource import CourseResource
from models import myunit


class CourseResourceTest(myunit.MyTest):
    u"""4.0PC模板课程-素材-创建"""
    sys.setrecursionlimit(150000)
    upload_time = 100  # 文件上传默认等待最长时间，文件过大时需增大
    file_url = 'D:\\test_input.txt'  # 文件路径
    big_file = 'D:\\50m.pdf'  # 文件路径
    ppt = 'D:\\wzk_python_selenium\\PC4.0\\files\\1.ppt'
    mp4 = 'D:\\wzk_python_selenium\\PC4.0\\files\\2.mp4'
    mp3 = 'D:\\wzk_python_selenium\\PC4.0\\files\\3.mp3'
    doc = 'D:\\wzk_python_selenium\\PC4.0\\files\\4.doc'
    # mp3 = 'D:\\wzk_python_selenium\\PC4.0\\files\\3.mp3'
    # doc = 'D:\\wzk_python_selenium\\PC4.0\\files\\4.doc'
    file_lists = [ppt , mp4, mp3, doc, ]  # 文件列表

    def test0001_batch_create_sucess001(self):
        u"""4.0PC模板课程-素材-批量上传成功："""
        resource = CourseResource(self.driver)
        resource.login()
        resource.enter_course_resource_page()  #进入组课-素材页面
        resource.batch_create_resource(file_lists=self.file_lists, type_text='专业标准', upload_time=10)

    def test0001_create_sucess001(self):
        u"""4.0PC模板课程-素材-创建成功：中文PPT演示文稿"""
        ppt = [self.ppt]
        resource = CourseResource(self.driver)
        resource.login()
        resource.enter_course_resource_page()  # 进入组课-素材页面
        resource.create_resource(apply_type='专业标准', mime_type='PPT演示文稿', language='中文', file_urls=ppt)

    def test0001_create_sucess002(self):
        u"""4.0PC模板课程-素材-创建成功：英文mp4"""
        mp4 = [self.mp4]
        resource = CourseResource(self.driver)
        resource.login()
        resource.enter_course_resource_page()  # 进入组课-素材页面
        resource.create_resource(apply_type='专业标准', mime_type='视频类', language='英文', file_urls=mp4)

    def test0001_create_sucess003(self):
        u"""4.0PC模板课程-素材-创建成功：大文件"""
        big_file = [self.big_file]
        resource = CourseResource(self.driver)
        resource.login()
        resource.enter_course_resource_page()  # 进入组课-素材页面
        resource.create_resource(apply_type='专业标准', mime_type='PPT演示文稿', language='中文', file_urls=big_file, upload_time=100)

    def test0002_create_fail001(self):
        u"""4.0PC模板课程-素材-创建失败：知识点不能为空"""
        ppt = [self.ppt]
        alert_info = "知识点不能为空"
        resource = CourseResource(self.driver)
        resource.login()
        resource.enter_course_resource_page()  # 进入组课-素材页面
        resource.create_resource(knowledge='', file_urls=ppt)
        self.assertIn(alert_info, resource.create_errors_info())

    def test0002_create_fail002(self):
        u"""4.0PC模板课程-素材-创建失败：应用类型不能为空"""
        ppt = [self.ppt]
        alert_info = "应用类型不能为空"
        resource = CourseResource(self.driver)
        resource.login()
        resource.enter_course_resource_page()  # 进入组课-素材页面
        resource.create_resource(apply_type='', file_urls=ppt)
        self.assertIn(alert_info, resource.create_errors_info())
