#Collect specific images on instgram (Just for study)
#Device : Apple Macbook Air M1
#Browser : GoogleChorme
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import wget
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

save_dir = "/Users/jerrybin/desktop/"  #Set where the pictures are stored. 

driver = webdriver.Chrome()  
driver.get("https://www.instagram.com/")

time.sleep(1) #Wait for page to load

username = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input') #Find the user input field with fullxpath.
password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input') #Find the user password field with fullxpath.
login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]') #Find the login botton

username.clear() #Clear to prevent default characters
username.send_keys('User name') #User name
password.clear() #Clear to prevent default characters
password.send_keys('password') #password
login.click()

time.sleep(5) #Wait for page to load

passes = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]') #Find the show me later button with fullxpath.
passes.click() #Click the show me later button.

time.sleep(3)

search_button = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="搜尋"]') #Find the search button with css_selector.
search_button.click() #Click the search button.

time.sleep(2)

search_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input') #Find the search field with the fullxpath.

time.sleep(2)

keyword = "#cat" #The keyword of the search.
search_field.send_keys(keyword) #key in the keyword.

time.sleep(1)

first1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div') #Find the top search result with fullxpath.
first1.click() #Click the top search result.

time.sleep(6)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "x1i10hfl")]'))) #Wait until the load is complete

for i in range(5):  #Scroll down the page for 5 times, to show more pictures.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

image_elements = driver.find_elements(By.XPATH, '//a[contains(@class, "x1i10hfl")]/div/div/img') #Find the loaded image.
image_urls = [image.get_attribute("src") for image in image_elements] #get the link of the pictures.

path = os.path.join(save_dir, keyword) #Create a file to store all the downloaded images, use keyword naming.
os.makedirs(path, exist_ok=True)


for i, url in enumerate(image_urls): #Donwload pics.
    save_as = os.path.join(path, f"{keyword}{i}.jpg")
    wget.download(url, save_as)
    print(f"Downloaded: {save_as}")


