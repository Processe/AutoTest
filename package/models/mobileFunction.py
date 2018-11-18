# coding=utf-8
# --author='fangfang'
from models.mobileDriver import Mobile
from models.path import get_obj_path
from models.logger import Logger
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
from screenshot import Screenshot

model = None
ifInstallMonkey = None
ifRunMonkey = None


logger = Logger(logger="function").getlog()

sep = os.path.sep  # 当前系统分隔符
timeout = 20
PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
    )


path = get_obj_path()


class ScriptError(Exception):
    '''
    返回报错信息类
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FunctionLibrary(object):
    def __init__(self, driver):
        # mobile = Mobile()
        # mobile_driver = Mobile()
        # self.mobile_driver = mobile.mobile_setConfig().driver
        self.mobile_driver = driver
        self.screenshot = Screenshot(driver, '异常截图', '')

    def excepTion(function):
        """
        异常装饰器，用来替代try except
        """
        def wrapper(*args, **keyargs):
            try:
                return function(*args, **keyargs)
            except Exception as e:
                # log the exception
                funcName = function.__name__
                self = args[0]
                # 组装异常信息
                paramsStr = "--".join([str(v) for k, v in enumerate(args) if k > 0])
                x = "[Error]:"+funcName+"--"+paramsStr+"  [异常信息：%s]" % repr(e)
                if funcName != "takeTakesScreenshot":
                    # 当异常信息不是来自于截图的时候才进行截图，防止因截图异常而引起死循环
                    self.screenshot.takeTakesScreenshot("异常截图", funcName)
                self.mobile_driver.quit()
                # 删除driver.ini文件
                # re-raise the exception
                raise ScriptError(x)
        return wrapper

    @excepTion
    def CheckByNameIsDisplayed(self, name):
        WebDriverWait(self.mobile_driver, 20).until(EC.visibility_of_element_located((By.NAME, name))).is_displayed()
        logger.info("The function checkByName By name is: %s" % name)

    @excepTion
    def ClearByname(self, name):
        element = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.NAME, name)))
        element.clear()
        logger.info("The function ClearByname By name is: %s" % name)

    @excepTion
    def ClearByID(self, element_id):
        element = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.ID, element_id)))
        element.clear()
        logger.info("The function ClearByID By element_id is: %s" % element_id)

    @excepTion
    def ClickByXpath(self, xpath):
        element = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.click()
        logger.info("The function ClickByXpath By name is: %s" % xpath)

    @excepTion
    def SendKeyByADB(self, content):
        os.system("adb shell input text '%s'" % content)
        logger.info("The function SendKeyByADB input: %s" % content)

    def getNumByRe(self, str1):
        import re
        model = re.compile(r"\d+")
        ss = model.findall(str1)
        s = ""
        for i in range(len(ss)):
            s += ss[i]
        return s

    def ClickByName(self, name):
        WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.NAME, name))).click()
        logger.info("The function ClickByName By name is: %s" % name)

    @excepTion
    def ClickByID(self, id):
        WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.ID, id))).click()
        logger.info("The function ClickByID By id is: %s" % id)

    @excepTion
    def ClickByClassName(self, className):
        el = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
        el.click()
        logger.info("The function ClickByClassName By className is: %s" % className)

    @excepTion
    def ClickByLinkText(self, linkText):
        '''
        根据链接文字进行点击
        '''
        el = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.LINK_TEXT, linkText)))
        el.click()
        logger.info("The function ClickByLinkText By linkText is: %s" % linkText)

    @excepTion
    def ClickByUiauto(self,  Uiauto):
        el = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.ANDROID_UIAUTOMATOR, Uiauto)))
        el.click()
        logger.info("The function ClickByUiauto By Uiauto is: %s" % Uiauto)

    @excepTion
    def SwipeToFindClickByName(self, name):
        for i in range(10):
            time.sleep(1)
            elements = self.mobile_driver.find_elements_by_name(name)
            if len(elements) > 0:
                elements[0].click()
                break
            else:
                if i < 9:
                    self.swipeOnScreenN(0.8, 0.8, 0.3, 0.3, 1)
        logger.info("The function SwipeToFindClickByName By name is: %s" % name)

    @excepTion
    def SendKeysByID(self, element_id, content):
        element = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.ID, element_id)))
        element.clear()
        element.send_keys(content)
        logger.info("The function SendKeysByID By element_id: %s input: %s" % (element_id, content))

    @excepTion
    def ClickZhangHao(self, ZhangHao):
        xpath="//android.widget.TextView[contains(@text,\"****\")]"
        for i in range(10):
            elements = self.mobile_driver.find_elements_by_xpath(xpath)
            IsFind = False
            index = 0
            for el in elements:
                index += 1
                text = el.get_attribute("text")
                if self.IsOne(text, ZhangHao):
                    el.click()
                    IsFind = True
                    break
            if index == len(elements) and IsFind is False:
                self.swipeOnScreenN(0.8, 0.8, 0.2, 0.2, 1)

    @excepTion
    def SendKeysByXpath(self, xpath, content):
        element = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.clear()
        element .send_keys(content)
        logger.info("The function SendKeysByXpath By xpath: %s input: %s" % (xpath, content))

    @excepTion
    def SendKeysByName(self, name, content):
        element = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.NAME, name)))
        # element.clear()
        element.send_keys(content)
        logger.info("The function SendKeysByName By name: %s input: %s" % (name, content))

    @excepTion
    def SendKeysUseAdbInputText(self, content):
        '''
            只支持数字，暂未支持字母
        '''
        for i in content:
            strCmd = 'adb -s %s shell input text "%s"'%(self.udid, content)
            subprocess.Popen(strCmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()

    def swipeOnScreenN(self, floatStartX, floatStartY, floatEndX, floatEndY, num):
        screen = self.mobile_driver.get_window_size()
        screenWidth = screen["width"]  # 当前手机的宽度
        screenHeight = screen["height"]  # 当前手机的高度
        for i in range(num):
            self.mobile_driver.swipe(screenWidth * floatStartX, screenHeight * floatStartY, screenWidth * floatEndX,
                              screenHeight * floatEndY)

    @excepTion
    def swipeToFindElement(self, name):
        for i in range(6):
            elements = self.mobile_driver.find_elements_by_xpath(name)
            if len(elements) > 0:
                break
            else:
                if i < 5:
                    self.swipeOnScreenN(0.9, 0.9, 0.2, 0.2, 1)

    @excepTion
    def swipeToFindElementByXpath(self, xpath):
        for i in range(6):
            elements = self.mobile_driver.find_elements_by_xpath(xpath)
            if len(elements) > 0:
                break
            else:
                if i < 5:
                    self.swipeOnScreenN(0.8, 0.8, 0.5, 0.5, 1)

    @excepTion
    def swipeToFindElementByText(self, name):
        for i in range(6):
            elements = self.mobile_driver.find_elements_by_name(name)
            if len(elements) > 0:
                break
            else:
                if i < 5:
                    self.swipeOnScreenN(0.9, 0.9, 0.2, 0.2, 1)


    @excepTion
    def waitNAME(self, name):
        '''
        等待某个ID出现，切换到新页面时填写，然后截图
        '''
        WebDriverWait(self.mobile_driver, timeout).until(EC.presence_of_element_located((By.NAME, name)))

    @excepTion
    def waitTime(self, wtime):
        '''
        :param time: 等待固定时长，单位/秒
        :return: 无
        '''
        time.sleep(wtime)

    def CheckContentText(self,element_id, text):
        el = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.ID, element_id)))
        content = el.get_attribute("text")
        if text in content:
            logger.info("---%s:对比数据成功---" % text)
        else:
            raise ScriptError("[Error]:结果中未找到对应text值【%s】" % text)

    @excepTion
    def CheckByText(self, element_id, text):
        el = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.ID, element_id)))
        content = el.get_attribute("text")
        if "****" in content:
            if self.IsOne(content, text) is False:
                raise ScriptError("[Error]:结果中未找到对应text值【%s】" % text)
        elif self.IsStrChangeNum(content) is True and text.isnumeric() is True:
            if self.IsNumSame(content, text) is False:
                raise ScriptError("[Error]:结果中未找到对应text值【%s】" % text)
        elif text not in content :
            raise ScriptError("[Error]:结果中未找到对应text值【%s】" % text)

    def IsOne(self, name, value):
        if value.isnumeric() is True:
            return self.IsOneNum(name, value)
        elif value.isnumeric() is False:
            return self.IsOneStr(name, value)

    def IsStrChangeNum(self,n):
        import re
        if re.search(r"[^\d,\.]", n):
            return False
        else:
            return True

    def IsNumSame(self, n1, n2):
        try:
            f1 = float(n1.replace(",", ""))
            f2 = float(n2)
            if f1 - f2 == 0:
                return True
            else:
                return False
        except Exception as e:
            funcName = sys._getframe().f_code.co_name
            self.screenshot.takeTakesScreenshot("异常截图",funcName)
            self.mobile_driver.quitDriver()
            raise ScriptError("[Error]:"+funcName+"--"+n1+"--"+n2+"  [异常信息：%s]"%repr(e))

    def IsOneNum(self, GetStr, NewStr):
        IsSame = False
        TheStart = False
        TheEnd = False
        GetStr = GetStr.strip().split(" ")[0]
        GetStrs = "-".join(GetStr.strip()).split("-")
        NewStrs = "-".join(NewStr.strip()).split("-")
        GetStrlen = len(GetStrs)
        NewStrlen = len(NewStrs)
        for i, j in zip(range(GetStrlen), range(NewStrlen)):
            if GetStrs[0] == "*":
                TheStart = True
                break
            else:
                if GetStrs[i] != "*":
                    if GetStrs[i] != NewStrs[j]:
                        TheStart = False
                        break
                    elif GetStrs[i] == NewStrs[j]:
                        TheStart = True
                elif GetStrs[i] == "*":
                    break
        for i, j in zip(range(GetStrlen-1, -1, -1), range(NewStrlen-1, -1, -1)):
            if GetStrs[GetStrlen-1] == "*":
                TheEnd = True
                break
            else:
                if GetStrs[i] != "*":
                    if GetStrs[i] != NewStrs[j]:
                        TheEnd = False
                        break
                    elif GetStrs[i] == NewStrs[j]:
                        TheEnd = True
                elif GetStrs[i] == "*":
                    break
        if TheStart is True and TheEnd is True:
            IsSame = True
        return IsSame

    def IsOneStr(self, name, value):
        if name == value:
            return True
        else:
            return False

    def elementIsExist(self, name):
        # elements = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_all_elements_located((By.NAME, name)), name + '----对象未找到')
        elements = self.mobile_driver.find_elements_by_name(name)
        if len(elements) > 0:
            return True
        else:
            return False

    def elementIsExistByID(self, id):
        # elements = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_all_elements_located((By.NAME, name)), name + '----对象未找到')
        elements = self.mobile_driver.find_elements_by_name(id)
        if len(elements) > 0:
            return True
        else:
            return False

    @excepTion
    def IsExistByIdClick(self, element_id):
        elements = self.mobile_driver.find_elements_by_id(element_id)
        if len(elements) > 0:
            elements[0].click()
            logger.info("ID为%s的对象存在，已点击！" % element_id)
        else:
            logger.info("ID为%s的对象不存在！" % element_id)

    @excepTion
    def getCJJLXQ(self, details):
        '''
        :param details:
        :return:获取页面出借记录详情数据值
        '''
        element_id = "com.ygjr.ycd.debug:id/tender_detail_tv_data"
        el = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located((By.ID, element_id)))
        texts = el.get_attribute('text').split()
        if details == '出借时间':
            return texts[0]
        elif details == '出借详细时间':
            return texts[1]
        elif details == '预期利率':
            return texts[2]
        elif details == '加息利率':
            return texts[3]
        elif details == '项目期限':
            return texts[4]
        elif details == '项目还款方式':
            return texts[5]
        elif details == '出借本金':
            return texts[6]
        elif details == '使用现金劵':
            return texts[7]
        elif details == '预期利息':
            return texts[8]
        elif details == '加息奖励':
            return texts[9]
        elif details == '到期时间':
            return texts[10]
        else:
            return "没有此数据项！"

    def dataCompare(self, newdata, olddata):
        if newdata == olddata:
            logger.info("数据%s和%s对比成功！" % (newdata, olddata))
        else:
            raise ScriptError("数据%s和%s对比失败！" % (newdata, olddata))




