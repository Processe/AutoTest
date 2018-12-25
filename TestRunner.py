# coding=utf-8
# --author='fangfang'

import os
import time
import unittest
from package.models import HTMLTestRunner

test_dir = './test_case/execute_case/'
report_dir = './report/'
# html报告文件路径
report_abspath = os.path.join(report_dir, "result" + time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + ".html")
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    fp = open(report_abspath, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        title=u'自动化测试报告,测试结果如下：',
    #                                        description=u'用例执行情况：')
    # 如果不用生成HTML文件
    runner = unittest.TextTestRunner()
    runner.run(discover)


