from bs4 import BeautifulSoup

with open('website.html',encoding="UTF-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.prettify())
atag=soup.find_all(name='a')
for tag in atag:
    print(tag.getText())
for tag in atag:
    print(tag.get("href"))

print(soup.find(name="h3").string)
print(soup.select(selector="#name"))