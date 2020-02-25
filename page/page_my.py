# 页面对象模块


# 对象库
import time

from selenium.webdriver.common.by import By

from base.base_example import BasePage, BaseHandle
from page.page_user_login import UserLoginProxy
from tools.untils import DriverUtil


class MyPage(BasePage):
    # 测试超链接
    def __init__(self):
        super().__init__()
        self.ceshi =(By.CSS_SELECTOR,"[data-id='qa']")
    # 找到测试按钮
    def mypage_find_ceshi(self):
        return self.base_find_element(self.ceshi)
# 操作层
class MyHandle(BaseHandle):
    # 实例化对象库
    def __init__(self):
        self.my_handle =MyPage()
    # 点击测试
    def handle_click_ceshi(self):
        self.base_click_element(self.my_handle.mypage_find_ceshi())
# 业务层
class MyProxy():
    # 实例化操作层
    def __init__(self):
      self.myproxy =  MyHandle()

    # 点击测试进入qa页面
    def go_qa(self):
        self.myproxy.handle_click_ceshi()

if __name__ == '__main__':
    driver = DriverUtil().get_driver()

    driver.get(" http://demo.zentao.net/user-login.html")

    user = UserLoginProxy()
    user.user_login()
    time.sleep(2)
    myp =MyProxy()
    myp.go_qa()
    time.sleep(2)
    DriverUtil.quit_driver()