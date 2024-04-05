from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keeps chrome open


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')


store = driver.find_elements(By.CSS_SELECTOR, value='#store b')
value = []
for item in store:
    div = item.text
    try:
        value.append(float(div.split('-')[1].strip().replace(',', '')))       
    except:
        pass

paths  = ['//*[@id="buyCursor"]', '//*[@id="buyGrandma"]' , '//*[@id="buyFactory"]' , '//*[@id="buyMine"]', '//*[@id="buyShipment"]', '//*[@id="buyAlchemy lab"]' , '//*[@id="buyPortal"]' , '//*[@id="buyTime machine"]']

five_minutes = time.time() + 60*5
five_seconds = time.time() + 5

while True:    
    click = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
    click.click()
    # time.sleep(0.01)
    if time.time() > five_seconds:        
        for i in range(len(value)-1,-1, -1): 
            count = float((driver.find_element(By.ID, value='money')).text) 
            if count >= value[i]:                
                click_store = driver.find_element(By.XPATH, value=paths[i])
                click_store.click()
        five_seconds = time.time() + 5
    
    if time.time() > five_minutes:
        cps = driver.find_element(By.ID, value='cps')
        print(cps.text)
        break

        
    
    
