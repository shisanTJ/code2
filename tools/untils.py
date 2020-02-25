# 浏览器驱动
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtil:
    # 驱动保存
    __driver =None
    # 驱动获取
    @classmethod
    def get_driver(cls):
        # 如果__dirver为空,没有浏览器对象,无法滞空
        # 先初始化浏览器对象,保存在driver
        if cls.__driver is None:
            cls.__driver =webdriver.Chrome()
            cls.__driver.maximize_window()
            # cls.__driver.implicitly_wait(20)
        return cls.__driver
    # 销毁驱动
    @classmethod
    def quit_driver(cls):
        # 如果__driver为空,这是不需要销毁
        # 非空的时候需要销毁
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver =None

def exists_text(text):
    driver =DriverUtil.get_driver()
    try:
        WebDriverWait(driver,3,0.5).until(lambda x:x.find_element(By.XPATH,"//*[text()='{}']".format(text)))
        return True
    except:
        return False
