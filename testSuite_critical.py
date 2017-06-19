import unittest
from test_LoginAPI import LoginAPITest
 
# get all tests from LoginAPITest class
login_API_test = unittest.TestLoader().loadTestsFromTestCase(LoginAPITest)
 
# create a test suite combining all test cases
#test_suite = unittest.TestSuite([login_API_test, login_page_test])
test_suite = unittest.TestSuite(login_API_test)

print '#### TESTS STARTED - PRESS CTR-C TO STOP AT ANYTIME ####'

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)