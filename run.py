"""
===============
Author:Nan Xi
Time:  
Email:nanxi0309@gmail.com
===============
"""
import unittest
from HtmlTestRunner import HtmlTestRunner
import time,logging
import sys

# path='D:\\gitlab\\YeZhu_zrk_uiauto'
# sys.path.append(path)

# 指定测试用例和报告的路径
test_dir = '../testcase'
report_dir = '../reports'
# 加载登录测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'test_login.py')
# 加载委托测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'submit_clew.py')
# 定义报告的文件格式
now = time.strftime('Login-%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+' test_report.html'
# 运行测试用例并生成测试报告
with open(report_name,'wb') as f:
    runner = HtmlTestRunner(stream = f,title = '登录测试报告', description = 'Ziroom Android app test report')
    logging.info('start run test case...')
    runner.run(discover)