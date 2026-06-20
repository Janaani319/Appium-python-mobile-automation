from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from typing import Any, Dict
import allure
import pytest
import time

class TestMySLT:

    @pytest.fixture(scope="function")
    def driver_setup(self):
        """Fixture to set up and tear down the driver"""
        cap: Dict[str, Any] = {
            "platformName": "Android",
            "appium:deviceName": "JRedmi12",
            "appium:udid": "0bea41af7d77",
            "appium:platformVersion": "15",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.slt.selfcare",
            "appium:appWaitActivity": "*.MainActivity",
            "appium:noReset": "true"
        }
        url = 'http://localhost:4723'
        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

        yield driver

        # Cleanup
        driver.quit()

    @allure.title("Test Successful Login to MYSLT App")
    @allure.step("Login with valid credentials")
    def test_successful_login(self, driver_setup):
        driver = driver_setup

        # Wait for app to load
        driver.implicitly_wait(10)

        # Find login elements using AppiumBy
        username = driver.find_element(AppiumBy.ID, "com.slt.selfcare:id/et_userName")
        password = driver.find_element(AppiumBy.ID, "com.slt.selfcare:id/et_password")
        login_btn = driver.find_element(AppiumBy.ID, "com.slt.selfcare:id/btn_login")

        # Enter credentials
        username.send_keys("0702463497")
        password.send_keys("0002139")
        login_btn.click()

        # Verify successful login - check for homepage element
        homepage_element = driver.find_element(AppiumBy.ID, "com.slt.selfcare:id/rl_notification")
        assert homepage_element.is_displayed(), "Homepage not displayed after login"

    @allure.title("SLT Fibre Form Test")
    def test_SLTFibreform_filling(self, driver_setup):
        driver = driver_setup
        time.sleep(5)

        try:
            # Navigate to SLT Fibre page
            sltFib = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="SLT Fibre"]')
            sltFib.click()
            time.sleep(3)

            # --- DROPDOWNS ---
            # Title dropdown
            title_dropdown = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/sp_title')
            title_dropdown.click()
            time.sleep(1)
            title_option = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Ms"]')
            title_option.click()
            time.sleep(1)

            firstName = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_firstName')
            firstName.send_keys("Malshani")

            lastName = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_lastName')
            lastName.send_keys("Janani")

            # Nationality dropdown
            nationality_dropdown = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/sp_nationality')
            nationality_dropdown.click()
            time.sleep(1)
            nationality_option = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Sri Lankan"]')
            nationality_option.click()
            time.sleep(1)


            #passPortNIC = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_passport')
            #passPortNIC.send_keys("200057903403")

            eMail = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_email')
            eMail.send_keys("janaanimalsha@gmail.com")

            # --- DATE FIELD ---
            # Usually need to click to open date picker
            #dob = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/tv_birth')
            #dob.click()
            #time.sleep(2)

            # Select date from date picker (example)
            # You'll need to inspect the date picker structure
            #ok_button = driver.find_element(AppiumBy.ID, 'android:id/button1')
            #ok_button.click()

            # Go back
            backBtn = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/btn_backFragment')
            backBtn.click()
            time.sleep(2)

            print("Form filled successfully!")

        except Exception as e:
            driver.save_screenshot("form_error.png")
            pytest.fail(f"Form test failed: {str(e)}")


    @allure.title("SLT Megaline Form Test")
    def test_SLT_MegalineForm_Filling(self,driver_setup):
        driver = driver_setup
        time.sleep(5)

        try:
            sltMegaline = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="SLT Megaline"]')
            sltMegaline.click()
            time.sleep(3)

            fName = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_firstName')
            fName.send_keys("Malshani")

            lName = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_lastName')
            lName.send_keys("Janani")

            NIC = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_nic')
            NIC.send_keys("200057903403")

            PeoTvCheckBox = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/item_checkPeo')
            PeoTvCheckBox.click()

            # Wait for navigation to complete
            time.sleep(3)

            # Go back to homepage (very important!)
            driver.back()

            # Wait to return to homepage
            time.sleep(2)

            print("Navigation test completed successfully!")

        except Exception as e:
                    driver.save_screenshot("form_error2.png")
                    pytest.fail(f"Form test failed: {str(e)}")



    @allure.title("SLT_4G_LTE Form Test")
    def test_slt4GLTE_Form_Filling(self,driver_setup):
        driver = driver_setup
        time.sleep(5)

        try:
            slt4GLTE = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="SLT 4G LTE"]')
            slt4GLTE.click()
            time.sleep(3)

            FName = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_firstName')
            FName.send_keys("Malshani")

            LName = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_lastName')
            LName.send_keys("Janani")

            NIC = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/et_nic')
            NIC.send_keys("200057903403")

            voiceCheckBox = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/item_checkVoice')
            voiceCheckBox.click()

            PeoTvCheckBox4GLTE = driver.find_element(AppiumBy.ID, 'com.slt.selfcare:id/item_checkPeo')
            PeoTvCheckBox4GLTE.click()

            # Wait for navigation to complete
            time.sleep(3)

            # Go back to homepage (very important!)
            driver.back()

            # Wait to return to homepage
            time.sleep(2)

            print("Navigation test completed successfully!")

        except Exception as e:
            driver.save_screenshot("form_error3.png")
            pytest.fail(f"Form test failed: {str(e)}")



    @allure.title("Value Added Services Testing")
    @allure.description("Storage")
    def test_Storage(self,driver_setup):
        driver = driver_setup
        time.sleep(3)

        storeService =driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(4)')
        storeService.click()

        # Wait for navigation to complete
        time.sleep(3)

        # Go back to homepage (very important!)
        driver.back()

        # Wait to return to homepage
        time.sleep(2)

        print("Test completed successfully!")

    @allure.description("SltGo")
    def test_SltGo(self, driver_setup):
        driver = driver_setup
        time.sleep(3)

        sltgo = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiSelector().className("android.widget.ImageView").instance(5)')
        sltgo.click()

        # Wait for navigation to complete
        time.sleep(3)

        # Go back to homepage (very important!)
        driver.back()

        # Wait to return to homepage
        time.sleep(2)

        print("Test completed successfully!")

    @allure.description("PEOTV GO")
    def test_PeoTvGo(self, driver_setup):
        driver = driver_setup
        time.sleep(3)

        peotvGo = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiSelector().className("android.widget.ImageView").instance(6)')
        peotvGo.click()

        # Wait for navigation to complete
        time.sleep(3)

        # Go back to homepage (very important!)
        driver.back()

        # Wait to return to homepage
        time.sleep(2)

        print("Test completed successfully!")

    @allure.description("Kaspersky")
    def test_kaspersky(self, driver_setup):
        driver = driver_setup
        time.sleep(3)

        kaspersky = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiSelector().className("android.widget.ImageView").instance(7)')
        kaspersky.click()

        # Wait for navigation to complete
        time.sleep(3)

        # Go back to homepage (very important!)
        driver.back()

        # Wait to return to homepage
        time.sleep(2)

        print("Test completed successfully!")















