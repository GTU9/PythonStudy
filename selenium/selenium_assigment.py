from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.melon.com/chart/index.htm")

songs= driver.find_elements(By.CSS_SELECTOR, '.ellipsis.rank01 a')
song_Top100=[]

for i in range(len(songs)):
    song_Top100.append({
        "rank": i + 1,
        "song": songs[i].text
    })

df = pd.DataFrame(song_Top100)
print(df)