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

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
assert title == "Web form"

driver.implicitly_wait(5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
