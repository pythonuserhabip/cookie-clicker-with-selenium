from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\development\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path))

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(by="css selector", value="#articlecount a")
# print(article_count.text)
# # article_count.click()
#
# all_portals = driver.find_element(by="link text", value="Community portal")
# # all_portals.click()
#
# search = driver.find_element(by="name", value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://orteil.dashnet.org/cookieclicker/")

big_cookie = driver.find_element(by="id", value="bigCookie")

while True:
    timeout = time.time() + 10
    while time.time() < timeout:
        big_cookie.click()

    add_ons_list = driver.find_elements(by="css selector", value="#products.unlocked.enabled")
    add_ons_list[-1].click()