# coding=utf-8
# --author='fangfang'

import os, sys
from models.mobileDriver import Mobile
from models.path import get_obj_path
from models.logger import Logger

sep = os.path.sep  # 当前系统分隔符
logger = Logger(logger="Screenshot").getlog()


class Screenshot():
    def __init__(self, driver, case_modle, case_id):
        # ---截图对比用到的数据
        self.screenShotNum = 0  # 案例截图顺序
        self.transName = ""
        self.case_id = case_id
        # self.case_id = os.path.basename(sys.argv[0]).split(".")[0]
        # self.case_modle = os.path.dirname(get_obj_path())
        self.case_modle = case_modle
        self.image_path = sep.join([get_obj_path(), 'result\\image\\'+self.case_modle, self.case_id])
        self.num = 0
        self.driver = driver
        # ---截图对比用到的数据end

    def takeTakesScreenshot(self, fileName, funcName = ''):
        '''
        截图函数
        '''
        line = ''
        if funcName == '':
            self.num += 1
        if 1 <= self.num < 10:
            line = "00"+str(self.num)
        elif 10 <= self.num < 100:
            line = "0"+str(self.num)
        elif 100 <= self.num < 1000:
            line = str(self.num)
        if not os.path.exists(self.image_path):
            os.makedirs(str(self.image_path))
            self.driver.get_screenshot_as_file(self.image_path+'/'+line+fileName+'.png')
        else:
            self.driver.get_screenshot_as_file(self.image_path+'/'+line+fileName+'.png')


    def getModlePath(self, path):
        father_path = os.path.dirname(os.path.abspath(__file__))
        father_path1 = father_path.split("\\")
        modle_path = ''
        for i in father_path1:
            if i != path:
                father_path1.remove(i)
                continue
            else:
                for t in father_path1:
                    print(father_path1)
                    modle_path = modle_path + '\\' + t
                return modle_path
        return modle_path



