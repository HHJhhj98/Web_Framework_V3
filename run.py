# -*- coding：utf-8 -*-
# @Time ：2022/2/22 23:03
# @Authon :hhj
# @Annotation:
# @File : run.py

import datetime

from Common.send_mail import SendMail
from TestCases.Test0LoginCases import test_00_login
from BeautifulReport import BeautifulReport
from HwTestReport import HTMLTestReport
from Common.project_path import *

import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.discover(test_case_path))
    # with open('test_report.html', 'wb') as file:
    #     #runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='测试报告', description='第一次测试报告', tester='hhj')
    #     runner = HTMLTestReport(stream=file, verbosity=2, title="单元测试报告", description="第一次报告", tester="hhj",
    #                             images=False)
    #     runner.run(suite)

    # now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    run = BeautifulReport(suite)
    path = test_report_path + '\测试报告' + str(now) + '.html'
    run.report(description='登录模块', filename='\测试报告' + str(now),
               log_path=test_report_path)
    # SendMail().send_mail(path)