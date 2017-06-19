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

# run the suite
######## NOTE: Need to fix, this will show every individual test while being run ##########
#unittest.TextTestRunner(verbosity=2).run(test_suite)
########## When it is sent into var it can't be viewed in terminal as test is running ########


print '#### TESTS STARTED - PRESS CTR-C TO STOP AT ANYTIME #### '

stream = StringIO()
stream.seek(0)
stream.read()

runner = unittest.TextTestRunner(stream=stream, verbosity=2)
result = runner.run(test_suite)

# True/False if all tests pass
#### NOTE: NEED TO FIGURE OUT HOW TO PRINT RUNNERS TO CONSOLE
#### NEED TO SEE RESULTS INDIVIDUALLY
endResult = result.wasSuccessful()
	

# print results to terminal	
print '------------ TEST RESULTS ------------'	
print '|-', result 
print '|-', {'is_pass' : endResult}
print '--------------------------------------'


# dateTime timestamp
timeStamp = datetime.datetime.now()

# data to be sent to CSV
resultsList = [endResult, timeStamp]

# write results to new row
with open('results.csv', 'a') as f:
	wr = csv.writer(f, quoting = csv.QUOTE_ALL)
	wr.writerow(resultsList)


#pprint(result.failures)
#stream.seek(0)
#print 'Test output\n', stream.read()