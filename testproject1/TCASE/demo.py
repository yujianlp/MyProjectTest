# coding=utf-8

import unittest

class Demo(object):
    def setUp(self):
        s = "hellolaopi"
        # if isinstance(s, unicode):  # 如果是unicode就直接编码不需要解码
        #     print s.encode('utf-8')
        # else:
        print s.decode('utf-8').encode('gb2312')
        print("测试")

    def tearDown(self):
        t = "buypier"
        if isinstance(t, unicode):  # 如果是unicode就直接编码不需要解码
            print t.encode('utf-8')
        # else:
        #     print t.decode('utf-8').encode('gb2312')
        print("测试")

if __name__ == '__main__':
    d = Demo()
    d.setUp()
    d.tearDown()