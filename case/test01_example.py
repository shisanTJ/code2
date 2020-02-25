import json
import time
import unittest

from parameterized import parameterized

from config import BASE_PATH
from page.page_bug_browse import BugBrowseProxy
from page.page_bug_create import BugCreateProxy
from page.page_my import MyProxy
from page.page_qa import QaProxy
from page.page_user_login import UserLoginProxy
from tools.untils import DriverUtil, exists_text

# 读取测试数据 [(),(),()]
def get_case_data():
    # 创建存放数据列表
    result = list()

    # 读取数据构造数据元祖,放到列表中
    # a.读取json文件
    with open(BASE_PATH + "/data/example.json", "r", encoding="utf-8") as f:
        python_data = json.load(f)
        # b.构造数据
        for data in python_data:
            bug_title = data.get("bug_title")
            expect = data.get("expect")
            result.append((bug_title, expect))
    # 返回存放数据列表
    return result

class TestLoginCreateBug(unittest.TestCase):
    driver =None
    @classmethod
    def setUpClass(cls):
        # 获取driver
        cls.driver =DriverUtil.get_driver()
        # 获取登录业务层
        cls.login =UserLoginProxy()
        # 获取用例业务层
        cls.my =MyProxy()
        # 获取提bug业务层
        cls.qa =QaProxy()
        # 获取bug浏览业务层
        cls.bug_browse =BugBrowseProxy()
        # 获取提bug编辑业务层
        cls.bug_create =BugCreateProxy()
        cls.driver.get(" http://demo.zentao.net/user-login.html")
        # 登录
        cls.login.user_login()
    def setUp(self):
        # 登录首页
        pass
    def tearDown(self):
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    @parameterized.expand(get_case_data())
    def test_create_bug(self,title,excpet):

        # 点击用例
        self.my.go_qa()
        # 点击bug
        self.qa.go_bug()
        # 点击提bug
        self.bug_browse.go_bug_create()
        # 创建新bug
        time.sleep(2)
        self.bug_create.create_bug(title)
        # 断言
        result =exists_text(excpet)
        self.assertTrue(result)