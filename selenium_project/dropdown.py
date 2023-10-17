import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(2)
drp1 = Select(driver.find_element(By.ID,'drop1'))
#select by visible text
#select by index
#select by value
drp1.select_by_visible_text("doc 2")

#count no of options in dropdown
print(len(drp1.options))

#capture All the options
all1=drp1.options
for opt1 in all1:
    print(opt1.text)