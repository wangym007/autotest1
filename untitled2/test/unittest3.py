#encoding:utf-8
from appium import webdriver
import time
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = "Appium"
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['udid'] = 'A02AECPA2BR8S'
        desired_caps['deviceName'] = 'A02AECPA2BR8S'
        desired_caps['appPackage'] = 'com.eno.xyzq.page.test'
        desired_caps['appActivity'] = 'com.eno.pages.support.Activity_login'
        desired_caps['appWaitActivity'] = 'com.eno.pages.support.Activity_login'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps['noReset'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_loginteleOK(self):
        self.driver.find_element_by_id("com.eno.xyzq.page.test:id/rb_my").click()
        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column1").is_displayed():
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/unlogin_rl").click()

        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/login_account").send_keys("18666666666")
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/btn_get_smscode").click()
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/verify_code").send_keys("111111")
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/fundacc_login_button").click()
        try:
            if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_login_name").is_displayed():
                print "pass"
        except Exception, e:
            print e
            print "fail"

        '''self.assertEqual(True, False)'''

    def test_logintelefail(self):
        self.driver.find_element_by_id("com.eno.xyzq.page.test:id/rb_my").click()
        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column1").is_displayed():
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column3").click()

        time.sleep(5)

        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
            self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='退 出']").click()
            time.sleep(10)
            self.driver.find_element_by_xpath("//android.widget.Button[@content-desc ='确定']").click()
            time.sleep(5)
            if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column1").is_displayed():
                self.driver.find_element_by_id("com.eno.xyzq.page.test:id/unlogin_rl").click()

        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/login_account").send_keys("18666666666")
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/btn_get_smscode").click()
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/verify_code").send_keys("111113")
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/fundacc_login_button").click()

        try:
            if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
                print "pass"
        except Exception, e:
            print e
            print "fail"





if __name__ == '__main__':
    unittest.main()
