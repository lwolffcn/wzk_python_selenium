# coding=utf-8
import unittest
import time
import os
import sys
from HTMLTestRunner import HTMLTestRunner
curPath = os.path.abspath(os.path.dirname(__file__))  # D:\wzk_python_selenium\PC4.0\testcase
rootPath = os.path.split(curPath)[0]  # D:\wzk_python_selenium\PC4.0
sys.path.append(rootPath)
from models import function

# 构造测试集
# test_dir= './'
test_dir = curPath  # D:\wzk_python_selenium\PC4.0\testcase
report_dir = rootPath + '\\report'  # D:\wzk_python_selenium\PC4.0\report
# test_dir2 = 'D:\\wzk_python_selenium\\PC4.0\\testcase\\'
# print(test_dir)
# print(report_dir)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*wzk44.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = '../report/'+now+'result.html'
    filename = 'D:/wzk_python_selenium/PC4.0/report/' + now + 'result.html'
    print(discover)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试结果', description='用例执行情况')
    runner.run(discover)
    fp.close()
    # function.send_mail(report_dir=report_dir)
