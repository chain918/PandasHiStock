import requests
from bs4 import BeautifulSoup

url = "https://histock.tw/stock/financial.aspx?no=2330&st=2" # HIstock
response = requests.get(url) # 使用requests的get方法把網頁抓下來
html_doc = response.text # text屬性就是html文件原始碼
soup = BeautifulSoup(response.text, "lxml") # 指定lxml作為解析器來建立Beautiful物件

a_tags = soup.find_all('tr')
#a_tags = soup.find_all('h3', class_=seoh3, id=None)
a_tags = [a.getText() for a in a_tags]
#a_tags = list(filter(lambda a_str: a_str.find('搜尋') != 0, a_tags))

for a in a_tags:
    print(a)