from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
# Setup CHrome Options
options = Options()
#options.add_argument(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
options.add_argument(r"C:\\Users\vyava\AppData\Local\Google\Chrome") 
options.add_argument("--disable-extensions")
options.add_argument("--no-first-run")
options.add_argument("--homepage-is-newtabpage=false")
driver = webdriver.Chrome(options=options)
driver.get(r"https://www.linkedin.com/feed/")
username_field = driver.find_element(By.XPATH,'//*[@id="username"]')
username_field.send_keys("intex51000@gmail.com")
password_field = driver.find_element(By.XPATH,'//*[@id="password"]')
password_field.send_keys("Intex@51000")
sign_in = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[4]/button')
sign_in.click()
post = driver.find_element(By.XPATH,'//*[@id="ember303"]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/p')
post.send_keys("Hello, this is a test post! using selenium and python for using agentic ai in linkedin post")
time.sleep(100)



soup= BeautifulSoup(driver.page_source, 'html.parser')

print(soup.title.text)

driver.quit()