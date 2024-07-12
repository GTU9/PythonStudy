from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

search_tool = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
search_tool.click()
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)