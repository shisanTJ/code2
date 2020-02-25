# 页面对象模块
# 创建对象库
import time

from selenium.webdriver.common.by import By

from base.base_example import BasePage, BaseHandle
from page.page_my import MyProxy
from page.page_qa import QaProxy
from page.page_user_login import UserLoginProxy
from tools.untils import DriverUtil


class BugBrowsePage(BasePage):
    def __init__(self):
        super().__init__()
        self.ti_bug =(By.CSS_SELECTOR,".pull-right>.btn-primary")
    # 提bug连接
    def bug_find_bug(self):
        return self.base_find_element(self.ti_bug)
# 操层
class BugBrowseHandle(BaseHandle):
    def __init__(self):
        self.bug_browse_handle =BugBrowsePage()
    # 提bug 点击
    def click_ti_bug(self):
        self.base_click_element(self.bug_browse_handle.bug_find_bug())
# 业务层
class BugBrowseProxy():
    def __init__(self):
        self.bug_browse_proxy =BugBrowseHandle()
    # 进入提bugu页面
    def go_bug_create(self):
        self.bug_browse_proxy.click_ti_bug()


if __name__ == '__main__':
    driver = DriverUtil().get_driver()

    driver.get(" http://demo.zentao.net/user-login.html")

    user = UserLoginProxy()
    user.user_login()
    time.sleep(2)
    myp =MyProxy()
    myp.go_qa()
    time.sleep(2)
    qp =QaProxy()
    qp.go_bug()
    time.sleep(2)
    ti_bug =BugBrowseProxy()
    ti_bug.go_bug_create()
    DriverUtil.quit_driver()