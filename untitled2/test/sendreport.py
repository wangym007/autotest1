#encoding:utf-8
import unittestddt
import unittest
import HTMLTestRunner

suite =unittest.TestSuite()
suite.addTest(unittest.makeSuite(unittestddt.MyTestCase))

filename = 'test.html'

fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
       stream=fp,
       title='appiumtest',
       description='测试报告')

runner.run(suite)

fp.close()