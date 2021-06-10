from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT = "Account_email"
PASSWORD = "password"

chrome_web_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_web_driver)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=107935524&keywords=python&location=Belgrade%2C%20Serbia")

login = driver.find_element_by_class_name("nav__button-secondary")
login.click()

# waiting for page to load
time.sleep(7)

username = driver.find_element_by_id("username")
username.send_keys(ACCOUNT)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(7)

save_for_later = driver.find_element_by_xpath('//*[@id="ember368"]/button')
save_for_later.click()