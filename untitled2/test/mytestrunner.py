import unittestddt
import unittest

cases = unittest.TestLoader().loadTestsFromTestCase(unittestddt.MyTestCase)
mysuite = unittest.TestSuite([cases])

#mysuite = unittest.TestSuite()
#mysuite.addTest(unittestdemo.MyTestCase("testLogInFailed"))
#mysuite.addTest(unittestdemo.MyTestCase("testLogInOK"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)