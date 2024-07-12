# 웹 페이지에서 데이터 가져오기
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
response.text

# 웹 페이지 데이터를 soup 객체에 담기
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title.getText())


# 기사 정보 출력하기
article_tag = soup.find(name="span", class_="titleline")
print(article_tag.a)


# 기사 제목 출력하기
article_text = article_tag.a.getText()
print(article_text)


# 기사 URL 출력하기
article_link = article_tag.a.get("href")
print(article_link)


# 기사 추천 수 출력하기
article_upvote = soup.find(name="span", class_="score").getText()
print(article_upvote)


# 모든 기사 정보 출력하기
articles = soup.find_all(name="span", class_="titleline")
print(articles)


# 모든 기사의 제목과 URL 주소 출력하기
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.a.getText()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)

print(article_texts)
print(article_links)


# 모든 기사의 추천 수 출력하기
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)

int(article_upvotes[1].split()[0])

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)


# 추천을 가장 많이 받은 기사의 제목과 URL 출력하기
largest_number = max(article_upvotes)
print(largest_number)

largest_index = article_upvotes.index(largest_number)
print(largest_index)

print(article_texts[largest_index])
print(article_links[largest_index])

