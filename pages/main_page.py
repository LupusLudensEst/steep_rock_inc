from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Locators
TEXT_IS_HERE = (By.XPATH, "//div[@class='hero-subtitle']")
PHONE_IS_HERE = (By.XPATH, "(//div[@class='top-link-title w-hidden-small w-hidden-tiny'])[3]")
LOGO_IS_HERE = (By.XPATH, "(//img[@src='https://uploads-ssl.webflow.com/5a44e540f6b9a40001be7bae/5a44f7fc80557a000179868e_Logo-New.svg'])[2]")

class MainPage(Page):

    # Verify text "Provided exclusively for BioPharmaceutical and medical device companies." is here
    def vrfy_txt_here(self, txt):
        wait = WebDriverWait(self.driver, 10)
        expected_text = 'PROVIDED EXCLUSIVELY FOR BIOPHARMACEUTICAL AND MEDICAL DEVICE COMPANIES.'
        sleep(1.5)
        actual_text = wait.until(EC.presence_of_element_located((TEXT_IS_HERE))).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # Verify phone "+1 718-576-1406" is here
    def vrf_phn_here(self, phone):
        wait = WebDriverWait(self.driver, 10)
        expected_text = '+1 718-576-1406'
        actual_text = wait.until(EC.visibility_of_element_located((PHONE_IS_HERE))).text
        print(f'Actual phone: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # Verify logo "https://uploads-ssl.webflow.com/5a44e540f6b9a40001be7bae/5a44f7fc80557a000179868e_Logo-New.svg" is here
    def vrf_logo_here(self):
        wait = WebDriverWait(self.driver, 10)
        if wait.until(EC.visibility_of_element_located((LOGO_IS_HERE))):
            print("Image is displayed")
        else:
            print("image is not displayed")

    # End of the above code
















