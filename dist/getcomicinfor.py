import requests as re
from bs4 import BeautifulSoup as bs
import json
import os

titles = ["超人气","新作","订阅","少年","少女","纯爱","潜力", "完结","四格","漫改"]
path = r"D:\learning\前端\vueclilianxi\comics\public\img"
mainPage = re.get("http://www.u17.com/")
mainPage.encoding = mainPage.apparent_encoding
document = bs(mainPage.text, 'lxml')
for (index, container) in enumerate(document.select(".v5_comic_list")):
    comic_infors = []
    filepath = path + '\\' + titles[index]
    os.mkdir(filepath)
    print(titles[index],"downloading")
    for li in container.select('.comic_list_slide_box li'):
        print(li)
        infor = {}
        img = li.find('img')
        infor['name'] = img['title']
        infor["types"] = li.find('p').get_text()
        with open("{}\\{}.jpg".format(filepath, infor['name']), 'wb') as fo:
            fo.write(re.get(img['xsrc']).content)
        comic_infors.append(infor)
    json.dump(comic_infors, open(filepath + "\\"  + 'infor.json','w'))
