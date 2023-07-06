from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://tsj.tw/") #This is a simple click game web.

blow = driver.find_element(By.ID, "click") #Find the "blow now" botton.
blow_count = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

items = [] #To get the purchase botton. 
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]')) #田字薯餅
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]')) #電動飛機杯
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]')) #田小班的 Ban 10 變身器

prices = [] #To get the prices.
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]')) #10 initial point.
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]')) #15 initial point.
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]')) #20 initial point.


actions = ActionChains(driver)

for i in range(5000): #Click the suck button for 5000 times.
    actions.move_to_element(blow).click().perform() #Click the "blow now" botton.
    count = int((blow_count.text.replace("您目前擁有", "").replace("技術點", ""))) #The number of points currently owne.
    for x in range(3):
        price = int(prices[x].text.replace("技術點", ""))
        if price <= count: #Check if you have enough credits to purchase.
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(items[x])
            upgrade_actions.click()
            upgrade_actions.perform()
            break



