# 用例执行
import unittest
from WECHAT.jb import testall
class testclassone(unittest.TestCase):
    def setUp(self):
        print("\n开始测试\n")
        pass
    def test(self):
        testall()
        pass
    def tearDown(self):
        print("\n测试结束")
        pass

if __name__ == '__main__':
    unittest.main()