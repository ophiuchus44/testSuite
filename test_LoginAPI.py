import unittest
from selenium import webdriver
import requests
import json

#load config file with credential data
with open('config.json') as config:
    data = json.load(config)

configName = data['username']
configPasswd = data['password']


class LoginAPITest(unittest.TestCase): 
    def test_login_API(self):
        response = requests.get('https://api.github.com/', auth=(configName,configPasswd))

        answer = []
        if "message" in response.content:
            answer.append(False)
        else:
            answer.append(True)

        self.assertTrue(answer[0])
 
if __name__ == '__main__':
    unittest.main()