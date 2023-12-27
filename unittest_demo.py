from appium import webdriver
from unittest import TestCase


class TestDemo(TestCase):
    # Up大写
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "10"
        caps["deviceName"] = "vivo NEX A"
        caps["appPackage"] = "com.NEW.sph"
        caps["appActivity"] = ".business.launch.splash.SplashActivity"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator1"
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

# 必须要以test开头
    def test_Demo(self):
        el1 = self.driver.find_element_by_id("com.NEW.sph:id/btn_submit")
        el1.click()

        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_phoneNumEt")
        el2.send_keys("15300051321")
        el3 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_pwdEt")
        el3.send_keys("789987")
        el4 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_loginBtn")
        el4.click()
        # el5 = self.driver.find_element_by_id("com.NEW.sph:id/dialog_notify_backBtn")
        # el5.click()
        el6 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search_hint")
        el6.click()
        el7 = self.driver.find_element_by_id("com.NEW.sph:id/activity_search_inputEt")
        el7.click()
        el7.send_keys("包")
        el8 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search")
        el8.click()

    # Down大写
    def tearDown(self):
        self.driver.quit()
