from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Dreo-Velocity-Oscillating-Bladeless-DR-HTF007/dp/B09MKPDJRT/")

name = driver.find_element(By.ID, value="productTitle")
print(f"The name of this product is {name.text}.")

rate = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[9]/div[5]/div[4]/div[3]/div/span[1]/span/span[1]/a/span")
print(f"The rate of this product is {rate.text}.")

price=driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[9]/div[5]/div[4]/div[14]/div/div/div[3]/div[1]/span[2]/span[2]/span[2]")
print(f"The price of this product is {price.text} USD.")