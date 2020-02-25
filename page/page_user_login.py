# 创建页面对象模块
import time

from selenium.webdriver.common.by import By

from base.base_example import BasePage, BaseHandle


# 对象层
from tools.untils import DriverUtil


class UserLoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = (By.LINK_TEXT, "测试甲")
        self.click_login = (By.CSS_SELECTOR, "#submit")

    # 定位测试甲
    def page_find_element(self):
        return self.base_find_element(self.username)

    # 定位登录
    def page_login(self):
        return self.base_find_element(self.click_login)
# 操作层
class UserLoginHandle(BaseHandle):
    # 实例化对象库的对象
    def __init__(self):
        self.user_login_page =UserLoginPage()
    # 测试甲点击
    def click_ceshi_jia(self):
        self.base_click_element(self.user_login_page.page_find_element())
    # 登录点击
    def click_login(self):
        self.base_click_element(self.user_login_page.page_login())

class UserLoginProxy():
    def __init__(self):
        # 实例化操作层的对象
        self.user_login_proxy=UserLoginHandle()
    def user_login(self):
        # 点击测试甲
        self.user_login_proxy.click_ceshi_jia()
        # 点击登录
        self.user_login_proxy.click_login()

if __name__ == '__main__':
    driver =DriverUtil().get_driver()

    driver.get(" http://demo.zentao.net/user-login.html")

    user =UserLoginProxy()
    user.user_login()
    time.sleep(2)

    DriverUtil.quit_driver()