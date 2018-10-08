#encoding:utf-8
from appium import webdriver
import time
import unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 配置appium服务关键字
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

    @data(('18666666661', '111111', '186****6661，欢迎您'), ('18666666666', '111111', '186****6666，欢迎您'))
    @unpack
    def test_loginteleOK(self,telenum,yzm,loginname):
        #进入我的页面
        self.driver.find_element_by_id("com.eno.xyzq.page.test:id/rb_my").click()
        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column1").is_displayed():
            #进入手机号登录页面
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/unlogin_rl").click()

        #输入正确手机号，验证码登录
        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/login_account").send_keys(telenum)
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/btn_get_smscode").click()
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/verify_code").send_keys(yzm)
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/fundacc_login_button").click()

        #断言是否登录成功
        loginokname = self.driver.find_element_by_id("tv_login_name").text
        try:
            self.assertEqual(loginname, loginokname)
            print "successlogin"
        except Exception,e:
            print "faillogin "+e



        #进入账号管理页面
        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_login_name").is_displayed():
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column3").click()
            time.sleep(5)

        #退出账号
        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
            self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='退 出']").click()
            time.sleep(10)
            self.driver.find_element_by_xpath("//android.widget.Button[@content-desc ='确定']").click()
            time.sleep(5)

        #确认退出
        try:
            if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column1").is_displayed():
             print "sucessout"
        except Exception, e:
            print e
            print "failout"

    @data(('18666666666', '111113'), ('18666666666', '111114'))
    @unpack
    def test_logintelefail(self,telenum,yzm):
        #进入我的页面
        self.driver.find_element_by_id("com.eno.xyzq.page.test:id/rb_my").click()
        self.driver.find_element_by_id("com.eno.xyzq.page.test:id/unlogin_rl").click()

        #输入错误账号密码登录
        if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/login_account").send_keys(telenum)
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/btn_get_smscode").click()
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/verify_code").send_keys(yzm)
            self.driver.find_element_by_id("com.eno.xyzq.page.test:id/fundacc_login_button").click()

        try:
            if self.driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
                print "pass"
        except Exception, e:
            print e
            print "fail"





if __name__ == '__main__':
    unittest.main()
