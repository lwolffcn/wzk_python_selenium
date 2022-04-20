# coding=utf-8
import sys
from pages.login_page import Loginpage
from models import myunit, function


class LoginTest(myunit.MyTest):
    u"""4.0PC登录"""
    sys.setrecursionlimit(150000)
    user = '13651115151'
    password = 'Lf11111111'
    password_md5 = 'f99fd31072fc12615874e3169471b093'

    def test0001_login_sucess001(self):
        u"""4.0PC登录成功"""
        alert_info = "欢迎登录"
        login_success = Loginpage(selenium_driver=self.driver)
        login_success.login(user=self.user, password=self.password_md5)
        # function.insert_image(self.driver)
        self.assertIn(alert_info, login_success.login_success_info())

    def test0002_login_fail001(self):
        u"""4.0PC登录失败:用户名不能为空"""
        alert_info = "用户名不能为空"
        login_fail = Loginpage(selenium_driver=self.driver)
        login_fail.open()
        login_fail.login(user='', password=self.password)
        self.assertIn(alert_info, login_fail.login_errors_info())

    def test0002_login_fail002(self):
        u"""4.0PC登录失败:密码不能为空"""
        alert_info = "密码不能为空"
        login_fail = Loginpage(selenium_driver=self.driver)
        login_fail.open()
        login_fail.login(user='13611111111', password='')
        self.assertIn(alert_info, login_fail.login_errors_info())

    def test0002_login_fail003(self):
        u"""4.0PC登录失败:用户名或密码错误"""
        alert_info = "用户名或密码错误"
        login_fail = Loginpage(selenium_driver=self.driver)
        login_fail.open()
        login_fail.login(user='13611111111', password='4234224')
        self.assertIn(alert_info, login_fail.login_errors_info())

    def test0002_login_fail004(self):
        u"""4.0PC登录失败:用户名或密码错误"""
        alert_info = "用户名或密码错误"
        login_fail = Loginpage(selenium_driver=self.driver)
        login_fail.open()
        login_fail.login(user='1361111122222111', password='12345678')
        self.assertIn(alert_info, login_fail.login_errors_info())


class OpenFileTest():
    def test_file(self):
        f = open(r'D:\wzk_python_selenium\PC4.0\files\test_input.txt')
        print(f)
