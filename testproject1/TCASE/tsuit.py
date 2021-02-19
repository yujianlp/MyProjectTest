#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Commonlib.HTMLTestRunner import HTMLTestRunner
import unittest
from TCASE.tcase import TCase

class T(unittest.TestCase):

    def test_suit(self):
        case_list = ['test_001', 'test_002', 'test_003', 'test_004']
        # 创建测试套件
        mysuit = unittest.TestSuite()

        # 循环将测试用例放到测试套件中
        for case in case_list:
            mysuit.addTest(TCase(case))

        # 创建测试运行器,设置为每一个测试用例生成测试报告，运行测试套件中的测试用例
        # unittest.TextTestRunner(verbosity=2).run(mysuit)

        # 生成html测试报告
        file_name = "../output.html"
        with open(file_name, 'wb')as f:
            HTMLTestRunner(
                stream=f,
                title='我的测试报告',
                description='简单的网页测试报告',
                verbosity=2
            ).run(mysuit)


if __name__ == '__main__':
    unittest.main()
