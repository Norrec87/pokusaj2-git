from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Selenium 2\chromedriver.exe")

driver.get("https://euw.op.gg/")

SN=driver.find_element_by_id("searchSummoner")

SN.send_keys("Liqid88")

driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[2]/div/form/button[2]/img").click()

driver.find_element_by_xpath("//*[@id='__next']/div[4]/dl/dd[4]/div/a/img").click()






