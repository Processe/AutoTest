# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 0014 下午 19:21
# @Author  : fangfang
# @File    : asset_items.py


from models.unittest_setup import Setup
from models.logger import Logger

logger = Logger(logger="template").getlog()


class AssetItem:
    def __init__(self, trade, caseid):
        self.trade = trade
        self.caseid = caseid

    def add_asset(self):
        # -------------实例化方法类----------
        case = Setup()
        case.asset_web_setup(self.trade, self.caseid)
        driver = case.driver
        functionlibrary = case.functionlibrary
        datatools = case.datatools
        screenshot = case.screenshot
        datas = datatools.getExcelDateRowsByValue(self.trade, self.caseid)

        # -----------业务流程逻辑-----------
        screenshot.takeTakesScreenshot("打开登录页面成功")
        functionlibrary.type("xpath", "//*[@id='app']/div/div/form/div[1]/div/div/input", int(datas[6]))
        functionlibrary.type("xpath", "//*[@id='app']/div/div/form/div[2]/div/div/input", datas[7])
        functionlibrary.click("xpath", "//*[@id='app']/div/div/form/div[3]/button")
        functionlibrary.sleep(5)
        screenshot.takeTakesScreenshot("登录成功截图")
        functionlibrary.click("xpath", "//*[@id='app']/div/div[1]/div[3]/div[3]/div/span")
        functionlibrary.forElementByClassnameClcik("el-dropdown-menu__item", "营业部")
        functionlibrary.sleep(3)
        # 新增进件菜单
        functionlibrary.click("xpath", "//*[@id='app']/div/div[2]/ul/li[5]")
        # 资产类型
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "1]/div/div/div/div/div[1]/input", "el-select-dropdown__item", datas[8])
        functionlibrary.sleep(2)
        # 手机号码
        functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[2]/div/div[1]/input", int(datas[9]))
        # 借款金额
        functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[3]/div/div/input", int(datas[10]))
        # 计息方式
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "4]/div/div/div[1]/input", "el-select-dropdown__item", datas[11])
        # 还款方式
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "5]/div/div/div[1]/input", "el-select-dropdown__item", datas[12])
        functionlibrary.sleep(2)
        # 还款期限
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "6]/div/div/div[1]/input", "el-select-dropdown__item", datas[13])
        # 金融产品
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "7]/div/div/div[1]/input", "el-select-dropdown__item", datas[14])
        # 客户来源
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "8]/div/div/div[1]/input", "el-select-dropdown__item", datas[15])
        # 车贷用途
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "9]/div/div/div[1]/input", "el-select-dropdown__item", datas[16])
        # 客户姓名
        functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[10]/div/div[1]/input", datas[17])
        # 身份证号码
        functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[11]/div/div[1]/input", datas[18])
        # 户籍地址
        functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[12]/div/div[1]/input", datas[19])
        # 民族
        functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[13]/div/div[1]/input", datas[20])
        # 性别
        functionlibrary.select_input_for_classname("//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div["
                                                   "14]/div/div/div[1]/input", "el-select-dropdown__item", datas[21])
        # 出生日期
        functionlibrary.type("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[15]/div/div[1]/input", datas[22])
        # 判断是否为联合信用贷，联合信用贷需要上传身份证正反面
        if datas[8] == "联合信用贷":
            # 身份证正面照片
            functionlibrary.click("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[17]/div/div/div/button")
            functionlibrary.execute_program("tools\\uploadIDCard.exe")
            functionlibrary.sleep(1)
            # 身份证反面照片
            functionlibrary.click("xpath", "//*[@id='app']/div/div[3]/div/div/div[3]/div[1]/form/div[18]/div/div/div/button")
            functionlibrary.execute_program("tools\\uploadIDCard.exe")
            functionlibrary.sleep(1)
        # 下一步
        functionlibrary.click("xpath", "//*[@id='app']/div/div[3]/div/div/div[1]/div[1]/span")
        functionlibrary.sleep(2)
        functionlibrary.click("xpath", "//*[@id='app']/div/div[3]/div/div/div[2]/div[2]/button[2]")
        functionlibrary.sleep(3)
        # 完成
        functionlibrary.click("xpath", "//*[@id='app']/div/div[3]/div/div/div[2]/div[2]/button[3]")
        functionlibrary.sleep(2)
        # 提示确定
        functionlibrary.click("xpath", "/html/body/div[11] /div/div[3]/button[2]")
        functionlibrary.sleep(5)
