# coding=utf-8
from selenium.webdriver.common.by import By
from models.base import Base


class Loginpage(Base):
    url = "/login/login"  # 验证url
    login_url = "http://wzk.36ve.com/login/login"

    def enter_login_page(self):
        """进入登录页面"""
        self.open()

    login_username_loc = (By.XPATH, "//input[@id='loginform-username']")  # 用户名
    login_password_loc = (By.XPATH, "//input[@id='loginform-password']")  # 密码
    login_button_loc = (By.XPATH, "//button[@type='submit']")  # 登录按钮

    def entry_login_detail(self, user='13651115151', password='f99fd31072fc12615874e3169471b093'):
        """输入用户名及密码"""
        self.wait_for(lambda: self.driver.find_element(*self.login_username_loc)).send_keys(user)
        self.wait_for(lambda: self.driver.find_element(*self.login_password_loc)).send_keys(password)

    password_md5 = 'f99fd31072fc12615874e3169471b093'

    def login(self, user='13651115151', password='f99fd31072fc12615874e3169471b093'):
        self.enter_login_page()  # 进入登录页面
        self.entry_login_detail(user=user, password=password)  # 输入用户名及密码
        self.button_click(tap_text='button', button_text='登录')  # 点击登录按钮登录

    login_success_loc = (By.XPATH, "//p[contains(text(),'欢迎登录')]")
    '''
    #用户名错误提示:
    用户名不能为空
    密码不能为空
    用户名或密码错误
    登录成功！
    '''
    # 登录失败验证
    def login_errors_info(self):
        return self.errors_info()

    # 登录成功验证
    def login_success_info(self):
        user_success = self.driver.find_element(*self.login_success_loc).text
        print(user_success)
        return user_success


if __name__ == "_main_":
    pass
