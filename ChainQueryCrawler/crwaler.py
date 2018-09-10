from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import time 
import json


#important not to wait until the page is complete
caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "eager"  #  interactive

driver = webdriver.Firefox()
driver.get("http://chainquery.com/bitcoin-api/getrawtransaction")

driver.find_element_by_css_selector("input[type='radio'][id='verbose'][value='1']").click()

input_element = driver.find_element_by_id("txid")
input_element.send_keys("492fcdecf0803a458c0240b4947063d5496df6f9b95056f33de73e391110f805")
input_element.send_keys(Keys.ENTER)
input_element.submit()
time.sleep(0.5)

soup = BeautifulSoup(driver.page_source,"html.parser")

elements = soup.find_all("pre")
elements = str(elements[0]).strip()
elements = elements[5:-6]
json_element = json.loads(elements)
print('elment:' + str(json_element))

driver.quit()