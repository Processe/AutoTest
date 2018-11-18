# -*- coding:utf-8 -*-


from configparser import ConfigParser
from selenium import webdriver
from models.logger import Logger
from models.path import get_obj_path

logger = Logger(logger="BrowserEngine").getlog()
dir_path = get_obj_path()
chrome_driver_path = dir_path + '/tools/chromedriver.exe'
ie_driver_path = dir_path + '/tools/IEDriverServer.exe'
config = ConfigParser()
# file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
file_path = dir_path + '/config/config.ini'
config.read(file_path)


class BrowserEngine(object):

    def __init__(self):
        self.browser = config.get("browserType", "browserName")
        self.url = config.get("webServer", "URL")
        # read the browser type from config.ini file, return the driver

    def open_browser(self):

        driver = "浏览器参数错误"
        if self.browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif self.browser == "Chrome":
            driver = webdriver.Chrome(chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif self.browser == "IE":
            driver = webdriver.Ie(ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(self.url)
        logger.info("Open url: %s" % self.url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    @ staticmethod
    def quit_browser(driver):
        logger.info("Now, Close and quit the browser.")
        driver.quit()
