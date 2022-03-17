import requests
from html5lib import html5parser
from  bs4 import BeautifulSoup

url=input("enter url :  ")
response=requests.get(url)
# print(response.text)
soup= BeautifulSoup(response.content, "html.parser")



anchor=soup.find_all('a') 
# for all anchor tags
all_link=set()

for links in anchor:
    if links in anchor:

        links_text="available urls        :   "+links.get('href')
        all_link.add(links)
        print(links_text)
