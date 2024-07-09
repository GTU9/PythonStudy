from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/s?k=fan")

prices = driver.find_elements(By.CSS_SELECTOR, value='.a-price-whole')
names = driver.find_elements(By.CSS_SELECTOR, value='h2 a span')
rates = driver.find_elements(By.CSS_SELECTOR, value=".a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom .a-icon-alt")
product_list = {}

for n in range(len(rates)):
    product_list[n] = {
        "name": names[n].text,
        "price": prices[n].text,
        "rate": rates[n].text,
    }
print(product_list)