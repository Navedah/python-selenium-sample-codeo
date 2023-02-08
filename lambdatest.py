
import unittest
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            'LT:Options': {
                "build": "Python Demo",  # Change your build name here
                "name": "Python Demo Test",  # Change your test name here
                "platformName": "Windows 11",
                "selenium_version": "4.0.0",
                "console": 'true',  # Enable or disable console logs
                "network": 'true',  # Enable or disable network logs
                #Enable Smart UI Project
                #"smartUI.project": "<Project Name>"
            },
            "browserName": "firefox",
            "browserVersion": "latest",
        }

        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot 
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/

        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=desired_caps)

# tearDown runs after each test case


    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_demo_site(self):

        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url

        try:
        
            print('Loading URL')
            driver.get("https://app.debonairspizza.co.za/")
            print('URL opened')
            sleep(10)

            # Let's click on a element
            driver.find_element("xpath",'/html/body/div[2]/div[2]/header/div/div[1]/button').click();
            sleep(3)

            driver.find_element("name",'mobileNumber').send_keys("");  #add your mobile number
            sleep(3)
            driver.find_element("xpath",'/html/body/div[2]/div[2]/main/div/div/div/div/div[1]/div/div/button').click();
            sleep(3)
            driver.find_element("name",'password').send_keys("");  #add your password
            sleep(3)
            driver.find_element("xpath",'/html/body/div[2]/div[2]/main/div/div/div/div/div[2]/div[3]/button').click();
            sleep(3)
            driver.find_element("xpath",'/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]').click();
            sleep(3)
            driver.find_element("xpath",'/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/nav/div/ul/li[4]/a').click();
            sleep(3)
            driver.find_element("xpath",'/html/body/div[2]/div[2]/main/div/div[2]/a[1]').click();
            sleep(3)
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
            
        except Exception as e: 
                        print(e)
                        # print(exception)                 
                        driver.execute_script("lambda-status=failed")


if __name__ == "__main__":
    unittest.main()