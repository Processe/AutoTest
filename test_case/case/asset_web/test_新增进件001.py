# coding=utf-8
# --author='fangfang'


from models.unittest_setup import Setup
import unittest


class TestXZJJ(unittest.TestCase):
    def setUp(self):
        """
        实例化基础类
        :return:
        """
        self.trade = "新增进件"
        self.caseid = "XZJJ-003"
        case = Setup()
        case.asset_web_setup(self.trade, self.caseid)
        self.driver = case.driver
        self.functionlibrary = case.functionlibrary
        self.datatools = case.datatools
        self.screenshot = case.screenshot

    def test_procedure(self):
        # -----获取测试数据------
        datas = self.datatools.getExcelDateRowsByValue(self.trade, self.caseid)
        # -----业务逻辑代码------
        self.screenshot.takeTakesScreenshot("打开登录页面成功")

        self.functionlibrary.type("xpath", "//*[@id='app']/div/div/form/div[1]/div/div/input", int(datas[6]))
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div/form/div[2]/div/div/input", datas[7])
        self.functionlibrary.click("xpath", "//*[@id='app']/div/div/form/div[3]/button")
        self.functionlibrary.sleep(5)
        self.screenshot.takeTakesScreenshot("登录成功截图")
        self.functionlibrary.click("xpath", "//*[@id='app']/div/div[1]/div[3]/div[3]/div/span")
        self.functionlibrary.forElementByClassnameClcik("el-dropdown-menu__item", "营业部")
        self.functionlibrary.sleep(3)
        # 新增进件菜单
        self.functionlibrary.click("xpath", "//*[@id='app']/div/div[2]/ul/li[5]")
        # 资产类型
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                          "1]/div/div/div/div/div[1]/input", 2, datas[8][0])
        self.functionlibrary.sleep(2)
        # 手机号码
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[2]/div/div["
                                           "1]/input", int(datas[9]))
        # 借款金额
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[3"
                                           "]/div/div/input", int(datas[10]))
        # 计息方式
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[4]/div/div/div["
                                          "1]/input", 3, datas[11][0])
        # 还款方式
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[5]/div/div/div["
                                          "1]/input", 4, datas[12][0])
        self.functionlibrary.sleep(2)
        # 还款期限
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[6]/div/div/div["
                                          "1]/input", 5, datas[13][0])
        # 金融产品
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[7]/div/div/div["
                                          "1]/input", 6, datas[14][0])
        # 客户来源
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[8]/div/div/div["
                                          "1]/input", 7, datas[15][0])
        # 车贷用途
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[9]/div/div/div["
                                          "1]/input", 8, datas[16][0])
        # 客户姓名
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[10]/div/div["
                                           "1]/input", datas[17])
        # 身份证号码
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[11]/div/div["
                                           "1]/input", datas[18])
        # 户籍地址
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[12]/div/div["
                                           "1]/input", datas[19])
        # 民族
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[13]/div/div["
                                           "1]/input", datas[20])
        # 性别
        self.functionlibrary.select_input("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[14]/div/div/div["
                                          "1]/input", 9, datas[21][0])
        # 出生日期
        self.functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[15]/div/div["
                                           "1]/input", datas[22])
        # 下一步
        self.functionlibrary.click("xpath", "//*[@id='app']/div/div[3]/div/div/div[2]/div[2]/button[2]")
        self.functionlibrary.sleep(3)
        # 完成
        self.functionlibrary.click("xpath", "//*[@id='app']/div/div[3]/div/div/div[2]/div[2]/button[3]")
        self.functionlibrary.sleep(2)
        # 提示确定
        self.functionlibrary.click("xpath", "/html/body/div[11] /div/div[3]/button[2]")
        self.functionlibrary.sleep(5)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭应用程序
        :return:
        """
        self.driver.quit()
