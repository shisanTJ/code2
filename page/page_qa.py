# 页面对象模块

# 对象库
import time

from selenium.webdriver.common.by import By

from base.base_example import BasePage, BaseHandle
from page.page_my import MyProxy
from page.page_user_login import UserLoginProxy
from tools.untils import DriverUtil


class QaPage(BasePage):
    def __init__(self):
        super().__init__()
        self.case =(By.CSS_SELECTOR,"[data-id='testcase']")
        self.bug =(By.CSS_SELECTOR,"[data-id='bug']")
    # 定位用例和bug
    def qa_find_case_element(self):
        return self.base_find_element(self.case)
    def qa_find_bug_element(self):
        return self.base_find_element(self.bug)
# 操作层
class QaHandle(BaseHandle):
    def __init__(self):
        self.qa_handle =QaPage()
    # 点击bug
    def qa_click_bug(self):
        self.base_click_element(self.qa_handle.qa_find_bug_element())
# 业务层
class QaProxy():
    def __init__(self):
        self.qa_proxy =QaHandle()
    # 点击bug
    def go_bug(self):
        self.qa_proxy.qa_click_bug()

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
    DriverUtil.quit_driver()