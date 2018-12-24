# coding=utf-8
# --author='fangfang'


'''
报文处理工具类
'''


import hashlib


class MessageTool:
    def sign(func):
        '''
        参数拼接转签名装饰器
        :param func:
        :return:
        '''

        def wrap(*args, **kwargs):
            a = ''
            for i in args:
                a = a + str(i) + '&'
            b = "aishangjie_1&" + a + "00&bed29568-f704-4090-a75b-fbf9adda9556"
            print(b)
            md = hashlib.md5()
            md.update(b.encode('utf-8'))
            s = md.hexdigest()
            func(s=s, *args, **kwargs)
            # return md.hexdigest()
            print("sign_s:" + s)

        return wrap

    def param_to_string(self, lists):
        '''
        参数列表拼接转化字符串
        :param lists:
        :return:
        '''
        string = ""
        a = ""
        for i in lists:
            a = a + str(i) + '&'
            string = a + "bed29568-f704-4090-a75b-fbf9adda9556"
        return string

    def encryption_md5(self, string):
        '''
        数据进行MD5加密
        '''
        md = hashlib.md5()
        md.update(string.encode('utf-8'))
        s = md.hexdigest()
        return s

    def dict_sorted_to_list(self, dicts):
        '''
        字典根据Key排序后，将排序后value转为列表
        :param dicts:
        :return:
        '''
        lists = []
        for k in sorted(dicts):
            if k != "sign":
                lists.append(dicts[k])
        return lists

