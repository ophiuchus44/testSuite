# testSuite
Practice designing and buidling a test suite using Python,Flask and Selenium. A github account, oSelenium, was set up specifically for this script but feel free to try it with your credentials (just edit the config file) !

In config file, update 'driver' to the location of your Selenium Driver.


To run all tests through Flask API --> ('python testAPI.py')
Once running, you will need to download Postman.

To run tests from API, go to any of the following URLs in PostMan and send a PUT requests (nothing needed in body)
http://localhost:8080/api/v1/login/all
http://localhost:8080/api/v1/login/critical
http://localhost:8080/api/v1/login/export




################ WITHOUT API ############################
To run full test suite  --> ('python testSuite_all.py')

To run full test suite and export results (only shows results of all Tests - not individual) --> ('python testSuite_export.py')

To run critial test suite --> ('python testSuite_critical.py')


Test_LoginAPI.py - This test checks credentials with Githubs API
Test_LoginUX.py - This test includes more 'User Experience' based testing with Selenium
