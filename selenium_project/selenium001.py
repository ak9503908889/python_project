# webdriver browser setup for launch
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)


#Billing Application - Login---

driver.get("https://rudramtech.in/billing-inventory/index.php")
print(driver.title)
driver.maximize_window()

driver.find_element(By.NAME,'txtregno').send_keys("9689")
time.sleep(2)

driver.find_element(By.ID,'exampleInputEmail').send_keys("9689")
time.sleep(2)

driver.find_element(By.NAME,'txtpassword').send_keys("billing@2023#(*)")
time.sleep(2)

driver.find_element(By.NAME,'sub').click()