import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import json

#load config file with credential data
with open('config.json') as config:
    data = json.load(config)

configName = data['username']
configPasswd = data['password']
configDriver = data['driver']

 
class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(inst):
        #### NOTE: add Firefox/Safari/Internet Explorer test cases ####
        # create a new Chrome session 
        inst.driver = webdriver.Chrome(configDriver)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
 
        #### NOTE: add incognito at some later point ####

        # navigate to the github login 
        inst.driver.get("http://www.github.com/login")

    def test_login_box(self):
        # check login box exists on Login page
        self.assertTrue(self.is_element_present(By.ID,"login_field"))

    def test_passwd_box(self):
        # check passwd box exists on Login page
        self.assertTrue(self.is_element_present(By.ID,"password"))

    def test_submit_btn(self):
        # check submit button exists on Login page
        self.assertTrue(self.is_element_present(By.XPATH,'//*[@id="login"]/form/div[4]/input[3]'))

    def test_login(self):
        # find where to send keys
        username = self.driver.find_element_by_id("login_field")
        password = self.driver.find_element_by_id("password")

#### NOTE: COME BACK AND PULL LOGIN FROM CONFIG FILE ####

        # send login credentials
        username.send_keys(configName)
        password.send_keys(configPasswd)

        # find button with xpath and submit
        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[3]').click()

    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()
 
    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
