from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless=new')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# 👉 load local file inside container
driver.get("file:///app/index.html")

driver.implicitly_wait(5)

text_box = driver.find_element(By.ID, "myInput")
submit_button = driver.find_element(By.TAG_NAME, "button")

text_box.send_keys("Hello")
submit_button.click()

message = driver.find_element(By.ID, "message")
value = message.text

print(value)

assert value == "Received!"

driver.quit()
