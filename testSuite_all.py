import unittest
from test_LoginUX import LoginTest
from test_LoginAPI import LoginAPITest
from StringIO import StringIO
from pprint import pprint
import csv
import datetime
 
# get all tests from LoginTest and LoginAPITest class
login_page_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
login_API_test = unittest.TestLoader().loadTestsFromTestCase(LoginAPITest)
 
# create a test suite combining all test cases
test_suite = unittest.TestSuite([login_API_test, login_page_test])
#test_suite = unittest.TestSuite(login_page_test)
#test_suite = unittest.TestSuite(login_API_test)


print '#### TESTS STARTED - PRESS CTR-C TO STOP AT ANYTIME ####'

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)