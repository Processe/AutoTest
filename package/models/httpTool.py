# coding=utf-8
# --author='fangfang'

import requests
import readConfig
from logger import Logger


class Http:
    def __init__(self):
        rc = readConfig.ReadConfig()
        self.scheme = rc.get_value("assetInterFace", "host")
        self.timeout = rc.get_value("assetInterFace", "timeout")
        self.log = Logger(logger="HTTP").getlog()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = self.scheme + url

    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_files(self, filename):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = 'F:/AppTest/Test/interfaceTest/testFile/img/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    # defined http get method
    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(self.timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.log("methed:get-----Time out!")
            return None

    # defined http post method
    # include get params and post data
    # uninclude upload file
    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data, timeout=float(self.timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.log("methed:post----Time out!")
            return None

    # defined http post method
    # include upload file
    def postWithFile(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.log("methed:postWithFile----Time out!")
            return None

    def getWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.log("method:getWithJson-----Time out!")
            return None

    # defined http post method
    # for json
    def postWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.log("method:postWithJson-----Time out!")
            return None

    def putWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.put(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.log("method:putWithJson-----Time out!")
            return None


if __name__ == "__main__":
    print("ConfigHTTP")

