# html 페이지 읽어오기
with open("website.html", encoding='UTF8') as file:
    contents = file.read()

# beatufulsoup 라이브러리로 html 페이지 파싱하기
from bs4 import BeautifulSoup

soup = BeautifulSoup(contents, "html.parser")

# 파싱된 정보 출력하기
soup
# print(soup)

# 페이지 타이틀 태그 정보 출력하기
soup.title
# print(soup.title.string)

# 페이지 타이틀 정보만 출력하기
soup.title.string
# print(soup.title.string)

# 들여쓰기가 적용된 html 내용 출력하기
# print(soup.prettify())

# a 태그 정보 출력하기
soup.a
# print(soup.a)

# 모든 a 태그 정보 출력하기
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# 모든 a 태그의 컨텐츠 정보 출력하기
# for tag in all_anchor_tags:
#     print(tag.getText())

# 모든 a 태그의 링크 정보 출력하기
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# 태그와 id 를 이용하여 정보 출력하기
heading = soup.find(name="h1", id="name")
# print(heading)

# 태그와 class 를 이용하여 정보 출력하기
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# p 태그 안에 있는 a 태그 정보만 출력하기
soup.select_one(selector="p a")
# print(soup.select_one(selector="p a"))

# id 가 name인 태그 정보 출력하기
soup.select_one(selector="#name")
# print(soup.select_one(selector="#name"))

# class 가 heading 인 코든 태그 정보 출력하기
soup.select(selector=".heading")
# print(soup.select_one(selector=".heading"))