from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# replit에만 있음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

print(browser.page_source)