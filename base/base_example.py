# 封装测试工具
# 页面基类--元素定位  操作层元素操作 业务层
# 公共基类
from selenium.webdriver.support.wait import WebDriverWait


from tools.get_log import GetLog
from tools.untils import DriverUtil
get_log =GetLog()
# 对象库层
class BasePage():
    def __init__(self):
        self.driver =DriverUtil.get_driver()

    # 定位元素
    def base_find_element(self,loc,time=20):
        # loc =定位策略,定位依据
        # 元素等待用显示等待

        wdw =WebDriverWait(self.driver,timeout=time,poll_frequency=0.5)
        element =wdw.until(lambda x:x.find_element(loc[0],loc[1]))
        get_log.get_logger().info("正在定位元素{}".format(loc))
        return element
# 操作层
class BaseHandle():
    # 元素啊操作点击 输入
    def base_input_text(self,element,text):
        # 清空
        element.clear()
        get_log.get_logger().info("正在清空")
        # 输入
        element.send_keys(text)
        get_log.get_logger().info("正在输入".format(text))

    def base_click_element(self,element):
        element.click()
        get_log.get_logger().info("正在点击")