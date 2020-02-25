# 组织运行测试用例
import time
import unittest

from case.test01_example import TestLoginCreateBug
# 创建测试套件
from config import BASE_PATH

suite =unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TestLoginCreateBug))

# 创建运行器
filename =BASE_PATH+ "/report/report{}.text".format(time.strftime("%Y%m%d%H%M%S"))

with open(filename,"w")as f:
    runner =unittest.TextTestRunner(stream=f,verbosity=2)

    runner.run(suite)