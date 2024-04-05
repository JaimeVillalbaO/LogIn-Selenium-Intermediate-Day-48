from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keeps chrome open


driver = webdriver.Chrome(options=chrome_options)

# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # print(number.text)


# article_count = driver.find_element(By.LINK_TEXT, value='Content portals')
# # article_count.click()

# search = driver.find_element(By.NAME, value='search')
# # search.send_keys('python')
# # search.send_keys(Keys.ENTER)

# # driver.close()

'''challenge'''

driver.get('https://secure-retreat-92358.herokuapp.com')
first_name = driver.find_element(By.CLASS_NAME, value='top')
first_name.send_keys('Jaime')
Last_name = driver.find_element(By.CLASS_NAME, value='middle')
Last_name.send_keys('Villalba')
email = driver.find_element(By.CLASS_NAME, value='bottom')
email.send_keys('jaime@gmail.com')

click = driver.find_element(By.XPATH, value='/html/body/form/button')
click.click()