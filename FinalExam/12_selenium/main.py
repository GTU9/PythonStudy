from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_option)

# driver.get("https://www.amazon.com/Dreo-Velocity-Oscillating-Bladeless-DR-HTF007/dp/B09MKPDJRT/")
#
# dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print(f"{dollar.text}$$")
#
# driver.quit()

driver.get(" https://janggoons.github.io/AdvancedPython/login-test/")

input_id=driver.find_element(By.NAME, value="id")
input_id.send_keys("123")

input_pw=driver.find_element(By.NAME, value="password")
input_pw.send_keys("123456")

input_email=driver.find_element(By.NAME, value="email")
input_email.send_keys("123@456")

btn=driver.find_element(By.TAG_NAME,value="button")
btn.click()