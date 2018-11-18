# coding=utf-8
# --author='fangfang'


from template.asset.web.asset_items import AssetItem
from template.ycd360.mobile.lend_record import LendRecord
import unittest


class TestXZJJ(unittest.TestCase):
    def setUp(self):

        self.trade = "新增进件"
        self.caseid = "XZJJ-008"

    def test_procedure(self):
        case = AssetItem(self.trade, self.caseid)
        case.add_asset()

    def test_app(self):
        case1 = LendRecord("出借记录", "CJJL_001")
        case1.lend_record()

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭应用程序
        :return:
        """

        pass
        # self.driver.quit()
