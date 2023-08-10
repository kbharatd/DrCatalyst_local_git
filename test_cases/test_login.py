import time

import allure
import pytest
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from utilities.Logger import LogGenerator
from pageObject.Login import LoginPage


class Test_Login:
    log = LogGenerator.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Validating opening of login page")
    @allure.issue("no issue")
    @allure.title("login page validation")
    @pytest.mark.sanity
    def test_page_title(self, setup):
        self.log.info("Start testing of test_page_title")
        self.log.info("Opening Browser")

        self.driver = setup

        self.log.info("Go to Url")

        if self.driver.title == "DrCatalystEHR":
            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site Practicing\\DrCatalystEHR\\Screenshots\\test_page_title_passed.png")
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_title case passed',
                          attachment_type=AttachmentType.PNG)
            self.log.info("test_page_title testing is passed")
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site Practicing\\DrCatalystEHR\\Screenshots\\test_page_title_failed.png")
            allure.attach(self.driver.get_screenshot_as_png(), name='test_page_title case failed',
                          attachment_type=AttachmentType.PNG)
            self.log.info("test_page_title testing is failed")
            assert False

        self.log.info("test_page_title testing os completed")

    @pytest.mark.reggression
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Validating error msg by giving wrong inputs")
    @allure.description("login with incorrect credentials to test error msg")
    def test_login(self, setup):
        self.log.info("Start testing of test_login")
        self.log.info("Opening Browser")
        self.driver = setup
        self.log.info("Go to Url")
        self.lp = LoginPage(self.driver)

        time.sleep(2)
        self.lp.Enter_Clinic_code("xyz")
        self.log.info("Enter Clinic Code--->xyz")

        self.lp.Enter_Username("abc")
        self.log.info("Enter Username---->abc")

        time.sleep(2)
        self.lp.Enter_Password("123")
        self.log.info("Enter Password---->123")

        time.sleep(1)

        self.lp.Click_login()
        self.log.info("Click on Login  Button")

        time.sleep(2)

        if self.driver.find_element(By.XPATH, "//span[@class='mtab-login-error-message']"):

            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site Practicing\\DrCatalystEHR\\Screenshots\\test_login_passed.png")

            allure.attach(self.driver.get_screenshot_as_png(), name='test_login case passed',
                          attachment_type=AttachmentType.PNG)

            self.log.info("test_login testing is passed")

            assert True

        else:
            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site Practicing\\DrCatalystEHR\\Screenshots\\test_login_failed.png")

            allure.attach(self.driver.get_screenshot_as_png(), name='test_login case failed',
                          attachment_type=AttachmentType.PNG)
            self.log.info("test_login testing is failed")
            assert False
        self.log.info("test_login testing os completed")
