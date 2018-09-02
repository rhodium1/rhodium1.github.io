import requests as re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


r = re.get("http://www.u17.com/")
r.encoding = r.apparent_encoding
rawHtml = r.text
soup = bs(rawHtml,'lxml')
loop = soup.select_one("#loop_container")
path = r'D:\learning\前端\vueclilianxi\comics\public\img\banner\\'
banner_img_urls = loop.find_all('a')


for (count, url) in enumerate(banner_img_urls):
    if("data-little" in url.attrs):
        littUrl = url['data-little']
        big_url = url['data-src']
        print("downloading {}".format(count))
        with open("{}banner_little{}.jpg".format(path, count),'wb') as fo:
            fo.write(re.get(littUrl).content)
        with open("{}banner_lg{}.jpg".format(path,count),'wb') as fo:
            fo.write(re.get(big_url).content)
    
