from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
LOGO_IS_HERE = (By.XPATH, "(//img[@src='https://uploads-ssl.webflow.com/5a44e540f6b9a40001be7bae/5a44f7fc80557a000179868e_Logo-New.svg'])[2]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.steeprockinc.com/' )

# 2. Verify logo "https://uploads-ssl.webflow.com/5a44e540f6b9a40001be7bae/5a44f7fc80557a000179868e_Logo-New.svg" is here
if wait.until(EC.visibility_of_element_located((LOGO_IS_HERE))) :
    print("Image is displayed")
else :
    print("image is not displayed")

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
