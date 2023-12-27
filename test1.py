# -*- coding: UTF-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "vivo NEX A"
caps["appPackage"] = "com.NEW.sph"
caps["appActivity"] = ".business.launch.splash.SplashActivity"
caps["autoGrantPermissions"] = "true"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)

el1 = driver.find_element_by_id("com.NEW.sph:id/btn_submit")
el1.click()

el2 = driver.find_element_by_id("com.NEW.sph:id/activity_login_phoneNumEt")
el2.send_keys("15300051321")
el3 = driver.find_element_by_id("com.NEW.sph:id/activity_login_pwdEt")
el3.send_keys("789987")
el4 = driver.find_element_by_id("com.NEW.sph:id/activity_login_loginBtn")
el4.click()
el5 = driver.find_element_by_id("com.NEW.sph:id/dialog_notify_backBtn")
el5.click()
el6 = driver.find_element_by_id("com.NEW.sph:id/tv_search_hint")
el6.click()
el7 = driver.find_element_by_id("com.NEW.sph:id/activity_search_inputEt")
el7.click()
el7.send_keys("包")
el8 = driver.find_element_by_id("com.NEW.sph:id/tv_search")
el8.click()

TouchAction(driver).tap(x=377, y=745).perform()
TouchAction(driver).press(x=475, y=1997).move_to(x=493, y=219).release().perform()

TouchAction(driver).long_press(el8).release().perform()

el9 = driver.find_element_by_id("com.NEW.sph:id/tv_buy")
el9.click()
el10 = driver.find_element_by_id("com.NEW.sph:id/tv_go_pay")
el10.click()
el11 = driver.find_element_by_id("com.NEW.sph:id/btn_pay")
el11.click()
driver.back()
driver.back()
driver.back()
el12 = driver.find_element_by_id("com.NEW.sph:id/btnLeft")
el12.click()
el13 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
el13.click()
el14 = driver.find_element_by_id("com.NEW.sph:id/btnLeft")
el14.click()
el15 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout")
el15.click()
el16 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[1]")
el16.click()
el17 = driver.find_element_by_id("com.NEW.sph:id/btnLeft")
el17.click()
driver.back()
driver.back()
driver.back()
driver.back()
el18 = driver.find_element_by_id("com.NEW.sph:id/iv_main_tab05")
el18.click()
el19 = driver.find_element_by_id("com.NEW.sph:id/btn_dialog_close")
el19.click()


driver.implicitly_wait(10)

driver.quit()