# coding=utf-8
# --author='fangfang'

import os
import time
import unittest
from package.models import HTMLTestRunner

test_dir = './test_case/execute_case/asset_interface'
report_dir = './report/'
# html报告文件路径
report_abspath = os.path.join(report_dir, "result" + time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + ".html")
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    # 生成HTML报告
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # # # 不用生成HTML文件
    # runner = unittest.TextTestRunner()

    # 执行器
    runner.run(discover)


