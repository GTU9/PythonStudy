from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Dreo-Velocity-Oscillating-Bladeless-DR-HTF007/dp/B09MKPDJRT/")

dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole")
cent=driver.find_element(By.CLASS_NAME,value="a-price-fraction")
print(f"The price of this product is ${dollar.text}.{cent.text}.")

stars = driver.find_element(By.XPATH, value='//*[@id="acrPopover"]/span[1]/a/span')
print(f"The stars of this product is {stars.text}.")

driver.quit()