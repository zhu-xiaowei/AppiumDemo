from time import sleep
from appium import webdriver

# 类名必须是Test开头
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:

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

    def test_buy(self):
        self.driver.find_element_by_id("com.NEW.sph:id/btn_submit").click()
        el2 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_phoneNumEt")
        el2.click()
        self.driver.set_value(el2, "15300051321")
        # el2.send_keys("15300051321")
        el3 = self.driver.find_element_by_id("com.NEW.sph:id/activity_login_pwdEt")
        el3.click()
        el3.send_keys("789987")
        self.driver.find_element_by_id("com.NEW.sph:id/activity_login_loginBtn").click()

        def loaded(driver, element_id):
            if len(driver.find_elements_by_id(element_id)) >= 1:
                driver.find_element_by_id(element_id).click()
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 5).until(loaded(self.driver, "com.NEW.sph:id/dialog_notify_backBtn"))
        except:
            print("finish find dialog_notify_backBtn")
        el6 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search_hint")
        el6.click()
        el7 = self.driver.find_element_by_id("com.NEW.sph:id/activity_search_inputEt")
        el7.click()
        el7.send_keys("包")
        el8 = self.driver.find_element_by_id("com.NEW.sph:id/tv_search")
        el8.click()
        el9 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]")
        el9.click()
        self.driver.find_element_by_id("com.NEW.sph:id/tv_buy").click()
        self.driver.find_element_by_id("com.NEW.sph:id/tv_go_pay").click()
        self.driver.find_element_by_id("com.NEW.sph:id/btn_pay").click()

    def teardown(self):
        # 在结束时停留在当前页面
        sleep(5)
        # pass
        self.driver.quit()
