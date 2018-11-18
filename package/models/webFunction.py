# coding=utf-8
from models.logger import Logger
import time
from models.screenshot import Screenshot
from configparser import ConfigParser
from models.path import get_obj_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os.path

dir_path = get_obj_path()
config = ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = dir_path + '\\config\\config.ini'
config.read(file_path)
# 定义查找元素时间
# print(file_path)
timeout = int(config.get("waiTime", "time"))
# create a logger instance
logger = Logger(logger="FunctionLibrary").getlog()


class ScriptError(Exception):
    '''
    返回报错信息类
    '''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FunctionLibrary(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver
        # quit browser and end testing

    def exception(function):
        """
        异常装饰器，用来替代try except
        """
        def wrapper(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except Exception as e:
                screenshot = Screenshot(self.driver, "", "异常截图")
                funcName = function.__name__
                # self = args[0]
                # 组装异常信息
                paramsStr = "--".join([str(v) for k, v in enumerate(args) if k > 0])
                x = "[Error]:" + funcName + "--" + paramsStr
                if funcName != "takeTakesScreenshot":
                    # 当异常信息不是来自于截图的时候才进行截图，防止因截图异常而引起死循环
                    screenshot.takeTakesScreenshot("异常截图")
                # self.quitDriver("1")
                # 删除driver.ini文件
                # 关闭webdriver
                self.driver.quit()
                logger.info(x)
                raise e

        return wrapper

    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    @exception
    def find_element(self, selector_by, selector_value):
        """

        :param selector:
        :return: element
        """
        element = None
        if selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
            logger.info("Had find the element  successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
            logger.info("Had find the element  successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
            logger.info("Had find the element  successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
            logger.info("Had find the element  successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
            logger.info("Had find the element  successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
            logger.info("Had find the element  successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
            logger.info("Had find the element successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
            logger.info("Had find the element  successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    @exception
    def find_elements_wait(self, selector_by, selector_value):
        """
        需要传入两个参数，查找元素类型和元素值
        函数返回element对象
        :param selector:
        :return: element
        """
        element = None
        if selector_by == 'id':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.ID, selector_value)))
            logger.info("Had find the element successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        elif selector_by == 'name':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.NAME, selector_value)))
        elif selector_by == 'class_name':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, selector_value)))
        elif selector_by == 'link_text':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.LINK_TEXT, selector_value)))
        elif selector_by == 'partial_link_text':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, selector_value)))
        elif selector_by == 'tag_name':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, selector_value)))
        elif selector_by == 'xpath':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, selector_value)))
            logger.info("Had find the element \' %s \' successful "
                        "by %s via value: %s " % (element.text, selector_by, selector_value))
        elif selector_by == 'css_selector':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector_value)))
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    # 输入
    def type(self, selector_by, selector_value, text):

        el = self.find_element(selector_by, selector_value)
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

            # 清除文本框

    def clear(self, selector_by, selector_value):

        el = self.find_element(selector_by, selector_value, )
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

            # 点击元素

    @exception
    def click(self, selector_by, selector_value):

        el = self.find_element(selector_by, selector_value)
        el.click()
        logger.info("The element \' %s \' was clicked." % el.text)

    @exception
    def send_keys_by_lements(self, selector_by, selector_value, content):
        '''
        三个参数：查找元素类型，元素熟悉值，send_keys方法输入值
        :param selector_by:
        :param selector_value:
        :param content:
        :return:
        '''
        element = self.find_elements_wait(selector_by, selector_value)
        # element[0].clear()
        element[0].send_keys(content)
        logger.info("Had type \' %s \' in inputBox" % content)

    @exception
    def click_by_element(self, selector_by, selector_value):
        '''
        三个参数：查找元素类型，元素熟悉值，send_keys方法输入值
        :param selector_by:
        :param selector_value:
        :param content:
        :return:
        '''
        element = self.find_elements_wait(selector_by, selector_value)
        element[0].click()
        logger.info("The element \' %s \' was clicked." % selector_value)

    @exception
    def forElementByClassnameClcik(self, calss_name, textContent):
        '''
        根据classname找出所有元素，再根据每个元素的textContent判断确定要操作的元素
        :param calss_name: 元素classname
        :param textContent: 原色的text值
        :return: 无
        '''
        elements = self.driver.find_elements_by_class_name(calss_name)
        length = len(elements)
        count = 0
        for i in elements:
            text = i.get_attribute("textContent")
            count += 1
            if text == textContent:
                i.click()
                logger.info("The element \' %s \' was clicked." % text)
                break
            else:
                if count >= length:
                    logger.info("Not found %s text." % textContent)

    def executeJS(self, js):
        '''
        执行JavaScript
        :param js: 索要执行的js
        :return: 无
        '''
        self.driver.execute_script(js)

    def select_input(self, input_xpath, div1_index, select_index):
        '''
        选项操作，操作两个xpath选择所选项
        :param input_xpath:输入框的xpath
        :param select_index:选项的index值
        :return:
        '''
        select_xpath = "/html/body/div[%s]/div[1]/div[1]/ul/li[%s]" % (div1_index, select_index)
        self.click('xpath', input_xpath)
        self.click('xpath', select_xpath)

    def select_input_for_classname(self, input_xpath, selecte_classname, text):
        '''
        循环classname对比text选择下拉项
        :param input_xpath: input的xpath
        :param selecte_classname: 选项的classname
        :param text: 选项的值
        :return:无
        '''
        self.click('xpath', input_xpath)
        self.forElementByClassnameClcik(selecte_classname, text)

    def set_value_xpath(self, xpath, value):
        '''
        强制对input赋值
        :param xpath: xpath
        :param value: 所赋的值
        :return: 无
        '''
        try:
            el = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].value = '%s';" % value, el)
            logger.info("The element \' %s \' was seted." % el.text)
        except NameError as e:
            logger.error("Not found %s xpath." % e)

    def execute_program(self, program_file):
        '''
        执行可执行程序
        :param program_file: 文件所在路径
        :return: 无
        '''
        file = dir_path + "\\" + program_file
        os.system(file)
