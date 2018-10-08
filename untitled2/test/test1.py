#encoding:utf-8
from appium import webdriver
import time


desired_caps = {}
desired_caps['automationName']="Appium"
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
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(10)

driver.find_element_by_id("com.eno.xyzq.page.test:id/rb_my").click()
if driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_column1").is_displayed():
    driver.find_element_by_id("com.eno.xyzq.page.test:id/unlogin_rl").click()

if driver.find_element_by_id("com.eno.xyzq.page.test:id/title").is_displayed():
    driver.find_element_by_id("com.eno.xyzq.page.test:id/login_account").send_keys("18666666666")
    driver.find_element_by_id("com.eno.xyzq.page.test:id/btn_get_smscode").click()
    driver.find_element_by_id("com.eno.xyzq.page.test:id/verify_code").send_keys("111111")
    driver.find_element_by_id("com.eno.xyzq.page.test:id/fundacc_login_button").click()
    str = driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_login_name").text
    str1 = u"186****6666，欢迎您"
    try:
        if driver.find_element_by_id("com.eno.xyzq.page.test:id/tv_login_name").is_displayed():
            print "pass"
    except Exception,e:
        print e
        print "fail"


time.sleep(10)

driver.quit()
