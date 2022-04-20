# coding=utf-8
import sys
from pages.course_model_resource import DelResource
from models import myunit


class DelResourceTest(myunit.MyTest):
    u"""4.0PC模板课程-素材-创建"""
    sys.setrecursionlimit(150000)
    # upload_time = 100  # 文件上传默认等待最长时间，文件过大时需增大
    # file_url = 'D:\\test_input.txt'  # 文件路径
    # file_url2 = 'D:\\50m.pdf'  # 文件路径
    # ppt = 'D:\\wzk_python_selenium\\PC4.0\\files\\1.ppt'
    # mp4 = 'D:\\wzk_python_selenium\\PC4.0\\files\\2.mp4'
    # mp3 = 'D:\\wzk_python_selenium\\PC4.0\\files\\3.mp3'
    # doc = 'D:\\wzk_python_selenium\\PC4.0\\files\\4.doc'
    # file_lists = [ppt , mp4, mp3, doc, ]  # 文件列表

    def atest0001_del_sucess001(self):
        u"""4.0PC模板课程-素材-批量上传成功："""
        del_test = DelResource(self.driver, base_url='http://wzk.36ve.com')
        del_test.login()
        del_test.enter_course_question_page()
        # sleep(2)
        # del_test.del_while()
        del_test.del_all()

    def test0001_del_sucess002(self):
        u"""4.0PC模板课程-素材-批量上传成功："""
        del_test = DelResource(self.driver, base_url='http://wzk.36ve.com')
        del_test.login()
        del_test.html_test()

