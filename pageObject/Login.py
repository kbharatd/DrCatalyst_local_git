import time

from selenium.webdriver.common.by import By


class LoginPage:
    Text_Clinic_XPATH = (By.XPATH, "//mtab-input-text[@id='clinic']//input[@type='TEXT']")
    Text_Username_XPATH = (By.XPATH, "//mtab-input-text[@id='username']//input[@type='TEXT']")

    Text_Password_XPATH = (By.XPATH, "//input[@type='PASSWORD']")

    Click_Login_XPATH = (By.XPATH, "//span[@class='ui-button-text ui-clickable']")

    Error_message_display_XPATH = (By.XPATH, "//div[@class='text-align-center']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Clinic_code(self, cliniccode):
        self.driver.find_element(*LoginPage.Text_Clinic_XPATH).send_keys(cliniccode)

    def Enter_Username(self, username):
        self.driver.find_element(*LoginPage.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def Click_login(self):
        self.driver.find_element(*LoginPage.Click_Login_XPATH).click()

    def Login_status(self):
        try:
            time.sleep(5)
            self.driver.find_element(*LoginPage.Error_message_display_XPATH)

            assert True

        except:
            assert False
