# coding=utf-8
import unittest
import time
import os
# import sys
import smtplib
from time import sleep
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def find_lastestfile(report_dir="D:\\wzk_python_selenium\\PC4.0\\report"):
    lists = os.listdir(report_dir)
    # 重新按时间对目录下的文件进行排列
    lists.sort(key=lambda fn: os.path.getmtime(report_dir+"\\"+fn))
    file = os.path.join(report_dir, lists[-1])
    return file
    

def send_mail(report_dir="D:\\wzk_python_selenium\\PC4.0\\report"):
    # 第三方邮件服务
    # 发送邮箱服务器
    smtpserver = "smtp.exmail.qq.com"
    # 发送用户名密码
    user = "feng.lin@36ve.com"
    password = "Linfeng068"
    # 发送邮箱
    sender = "feng.lin@36ve.com"
    # 接收邮箱
    receiver = "aalaiyezhi@163.com"
    # 发送邮箱主题
    subject = "Python SMTP 邮件测试"
    # 格式化当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    '''
    编辑邮件正文
    now1 = time.strftime("%Y-%m-%d %H-%M-%S")
    msg = MIMEText(now1,"html","utf_8")
    msg["Subject"] = Header(subject,"utf_8")
    msg["from"] = "lwolffcn@163.com"
    msg["to"] = "aalaiyezhi@163.com"
    '''
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    # 邮件正文内容
    message.attach(MIMEText(now+'Python 用例执行结果文件……', 'plain', 'utf-8'))
    # 编辑邮件附件
    attname = "E:\\selenium\\report\\1.txt"
    # with open(attname) as sendfile:
    #     lines = sendfile.readlines()
    # sendfile = open(attname, "rb").read()
    sendfile = open(find_lastestfile(report_dir=report_dir), "rb").read()
    # sendfile.closed
    att = MIMEText(sendfile, "base64", "utf_8")
    att["Content-Type"] = "application/octet-stream_command"
    att["Content-Disposition"] = "attachment;filename=result.html"
    # msgRoot = MIMEMultipart("related")
    # 添加附件
    message.attach(att)
    # 连接发送邮件
    '''
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, message.as_string())
    smtp.quit()
    print("邮件发送成功")
    '''
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, message.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    # sendfile = open(attname,"rb").close()

    
def insert_image(driver):
    # 定义文件目录
    driver.get_screenshot_as_file("e:\\baidu.png")
    driver.save_screenshot("e:\\baidu2.png")
    print("截图成功")


def zyk_login():
    # 定义文件目录
    print("截图成功")


def zyk_switch_window(driver):
        current_handle = driver.current_window_handle
        handles = driver.window_handles
        '''
        print("handles长度= %s"%len(handles))
        print(handles)
        #使用切片
        print("未切片")
        for handle in handles:
            print(handle)
        print("已切片")
        for handle in handles[-2:]:
            print(handle)
        '''
        for handle in handles[-2:]:
            if handle != current_handle:
                driver.switch_to.window(handle)
                # print("窗口切换成功")
                break
        # print("切换窗口成功")
        sleep(1)

            
def zyk_switch_windows(driver):
        current_handle = driver.current_window_handle
        handles = driver.window_handles
        for handle in handles:
            if handle != current_handle:
                driver.switch_to.window(handle)
                # print("窗口切换成功")
                break
        # print("切换窗口成功")
        sleep(1)
