from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\development\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path))

driver.get("https://www.python.org/")
# price = driver.find_element(by="class name", value="a-price-whole")
# print(price.text)

# documentation = driver.find_element(by="css selector", value=".documentation-widget a")
# print(documentation.text)

event_times = driver.find_elements(by="css selector", value=".event-widget time")
event_names = driver.find_elements(by="css selector", value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

