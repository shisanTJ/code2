# 页面对象模块
# 创建对象库
import time

from selenium.webdriver.common.by import By

from base.base_example import BasePage, BaseHandle
from page.page_bug_browse import BugBrowseProxy
from page.page_my import MyProxy
from page.page_qa import QaProxy
from page.page_user_login import UserLoginProxy
from tools.untils import DriverUtil


class BugCreatePage(BasePage):
    def __init__(self):
        # 影响版本 点击opened_build
        # 点击第一个build
        # bug标题title
        # 保存save

        super().__init__()
        self.opened_build = (By.CSS_SELECTOR, "#openedBuild_chosen")
        self.build = (By.CSS_SELECTOR, "#openedBuild_chosen [data-option-array-index='0']")
        self.bug_title = (By.CSS_SELECTOR, "#title")
        self.save_submit = (By.CSS_SELECTOR, "#submit")

    # 查找到版本
    def create_find_opened_build(self):
        return self.base_find_element(self.opened_build)

    # 查找到第一个版本
    def create_find_build(self):
        return self.base_find_element(self.build)

    # 查找bug标题
    def find_bug_title(self):
        return self.base_find_element(self.bug_title)

    # 查找保存
    def find_save_submit(self):
        return self.base_find_element(self.save_submit)


# 操作层
class BugCreateHandle(BaseHandle):
    def __init__(self):
        self.bug_create_handle = BugCreatePage()
    # 点击版本
    def click_opened_build(self):
        self.base_click_element(self.bug_create_handle.create_find_opened_build())
    # 点击第一个
    def click_build(self):
        self.base_click_element(self.bug_create_handle.create_find_build())
    # 输入标题
    def input_bug_title(self,title):
        self.base_input_text(self.bug_create_handle.find_bug_title(),title)
    # 点击保存
    def click_save_submit(self):
        self.base_click_element(self.bug_create_handle.find_save_submit())
    # 业务层
class BugCreateProxy():
    def __init__(self):
        self.bug_create_proxy=BugCreateHandle()

    def create_bug(self,title):
        self.bug_create_proxy.click_opened_build()
        self.bug_create_proxy.click_build()
        self.bug_create_proxy.input_bug_title(title)

        DriverUtil().get_driver().execute_script("window.scrollTo(0,10000)")

        self.bug_create_proxy.click_save_submit()

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
    time.sleep(2)
    create_bug =BugCreateProxy()
    create_bug.create_bug("iu")
    time.sleep(2)
    DriverUtil.quit_driver()