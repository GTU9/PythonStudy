import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.billboard.com/charts/hot-100/')
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find_all(name="h3", id="title-of-a-story")

song_name=[]
rank=[]
rank_default=0

for article in article_tag:
    song=article.getText()
    song_name.append(song.strip())
    rank_default+=1
    rank.append(rank_default)

song_data = {
    'rank':rank,
    'song_name':song_name,
}


df = pd.DataFrame(song_data)

print(df.head(10))