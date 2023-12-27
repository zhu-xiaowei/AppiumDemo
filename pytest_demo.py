import datetime
from time import sleep

import pytest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 类名必须是Test开头
class TestDemo:
    user_info = yaml.safe_load(open("user_info.yaml", "r"))
    print(user_info)

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "10"
        caps["deviceName"] = "vivo NEX A"
        caps["appPackage"] = "com.NEW.sph"
        caps["appActivity"] = ".business.launch.splash.SplashActivity"
        # 自动同意权限
        caps["autoGrantPermissions"] = "true"
        # caps["ensureWebviewsHavePages"] = True
        caps["automationName"] = "UiAutomator2"
        # 让输入中文更稳定 建议都加上
        # caps["unicodeKeyboard"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待10秒
        self.driver.implicitly_wait(10)

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.NEW.sph:id/btn_submit")
        el1.click()

        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_phoneNumEt")
        el2.click()
        el2.send_keys("15300051321")
        el3 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_pwdEt")
        el3.click()
        el3.send_keys("789987")
        el4 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_loginBtn")
        el4.click()
        el5 = self.driver.find_element_by_id("com.NEW.sph:id/dialog_notify_backBtn")
        el5.click()
        el6 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search_hint")
        el6.click()
        el7 = self.driver.find_element_by_id("com.NEW.sph:id/activity_search_inputEt")
        el7.click()
        el7.send_keys("包")
        el8 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search")
        el8.click()

    # 测试输入中文
    def test_unicode_input(self):
        el1 = self.driver.find_element_by_id("com.NEW.sph:id/btn_submit")
        el1.click()
        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_closeBtn")
        el2.click()
        el6 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search_hint")
        el6.click()
        el7 = self.driver.find_element_by_id("com.NEW.sph:id/activity_search_inputEt")
        el7.click()
        el7.send_keys("包")

    # 显式等待
    def test_wait(self):
        el1 = self.driver.find_element_by_id("com.NEW.sph:id/btn_submit")
        el1.click()
        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_phoneNumEt")
        el2.click()
        el2.send_keys("15300051321")
        el3 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_pwdEt")
        el3.click()
        el3.send_keys("789987")
        el4 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_loginBtn")
        el4.click()

        # 方式1 使用sleep硬判断 find_elements_by_id 返回数组
        # sleep(5)
        # if len(self.driver.find_elements_by_id("dialog_notify_backBtn")) >= 1:
        #     self.driver.find_element_by_id("com.NEW.sph:id/dialog_notify_backBtn").click()

        # 方式2 WebDriverWait+lambada 找不到 点击肯定会报错 不建议使用
        # WebDriverWait(self.driver,15).until(lambda x: len(self.driver.find_elements_by_id("dialog_notify_backBtn"))>1)
        # self.driver.find_element_by_id("dialog_notify_backBtn").click()

        # 方式3 Appium提供了封装好的方法 但是 当没有找到时 下面的点击依旧会报错
        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID), "dialog_notify_backBtn")
        # )
        # self.driver.find_element_by_id("dialog_notify_backBtn").click()

        # 方式4 自定义函数
        def loaded(driver):
            print(datetime.datetime.now())
            if len(self.driver.find_elements_by_id("dialog_notify_backBtn")) >= 1:
                self.driver.find_element_by_id("dialog_notify_backBtn").click()
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 10).until(loaded)
        except:
            print("has permission")

        # el5 = self.driver.find_element_by_id("com.NEW.sph:id/dialog_notify_backBtn")
        # el5.click()
        el6 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search_hint")
        el6.click()
        el7 = self.driver.find_element_by_id("com.NEW.sph:id/activity_search_inputEt")
        el7.click()
        el7.send_keys("包")
        el8 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search")
        el8.click()

    def test_xpath(self):
        el1 = self.driver.find_element_by_id("com.NEW.sph:id/btn_submit")
        el1.click()
        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_closeBtn")
        el2.click()
        el3 = self.driver.find_element_by_xpath("//*[@text='直播'] and contains(@resource-id,'main_tab')")
        el3.click()

    @pytest.mark.parametrize("phone_number,msg_code,user_name", [
        ("15300051321", "789987", "LV脾气"),
        ("17319332997", "789987", "carlwe"),
        ("15104020310", "789987", "糖糖糖")
    ])
    def test_login(self, phone_number, msg_code, user_name):
        self.driver.find_element_by_id("com.NEW.sph:id/btn_submit").click()
        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_phoneNumEt")
        el2.click()
        el2.send_keys(phone_number)
        el3 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_pwdEt")
        el3.click()
        el3.send_keys(msg_code)
        self.driver.find_element_by_id("com.NEW.sph:id/activity_login_loginBtn").click()

        def loaded(driver, element_id):
            if len(driver.find_elements_by_id(element_id)) >= 1:
                driver.find_element_by_id(element_id).click()
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 5).until(loaded(self.driver, "dialog_notify_backBtn"))
        except:
            print("finish find dialog_notify_backBtn")

        self.driver.find_element_by_id("com.NEW.sph:id/iv_main_tab05").click()

        try:
            WebDriverWait(self.driver, 5).until(loaded(self.driver, "btn_dialog_close"))
        except:
            print("finish find btn_dialog_close")

        el8 = self.driver.find_element_by_id("userNameTv")
        print(el8.text)
        assert user_name == el8.text

    @pytest.mark.parametrize("phone_number,msg_code,user_name", user_info)
    def test_login_yaml(self, phone_number, msg_code, user_name):
        self.driver.find_element_by_id("com.NEW.sph:id/btn_submit").click()
        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_phoneNumEt")
        el2.click()
        el2.send_keys(phone_number)
        el3 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_pwdEt")
        el3.click()
        el3.send_keys(msg_code)
        self.driver.find_element_by_id("com.NEW.sph:id/activity_login_loginBtn").click()

        def loaded(driver, element_id):
            if len(driver.find_elements_by_id(element_id)) >= 1:
                driver.find_element_by_id(element_id).click()
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 5).until(loaded(self.driver, "dialog_notify_backBtn"))
        except:
            print("finish find dialog_notify_backBtn")

        self.driver.find_element_by_id("com.NEW.sph:id/iv_main_tab05").click()

        try:
            WebDriverWait(self.driver, 5).until(loaded(self.driver, "btn_dialog_close"))
        except:
            print("finish find btn_dialog_close")

        el8 = self.driver.find_element_by_id("userNameTv")
        print(el8.text)
        assert user_name == el8.text

    def teardown(self):
        # 在结束时停留在当前页面
        sleep(3)
        # pass
        self.driver.quit()
