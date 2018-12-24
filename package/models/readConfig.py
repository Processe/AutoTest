# coding=utf-8
# --author='fangfang'

from configparser import ConfigParser
import path

config_file = path.get_obj_path() + "\\config\\config.ini"

class ReadConfig:
    def __init__(self):
        self.config = ConfigParser()
        # self.config.read(config_file)

    def get_value(self, config_type, config_value):
        '''
        获取配置文件内容
        :param config_type: 类型
        :param config_value: 内容
        :return:值
        '''
        self.config.read(config_file)
        value = self.config.get(config_type, config_value)
        return value

