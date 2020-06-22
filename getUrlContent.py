import re
import requests
import json
from bs4 import BeautifulSoup


def get_HTML(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"}
    try:
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  # 指定编码形式
        return r.text
    except:
        return "please inspect your url or setup"

# 解析目标网页的html


def get_information_from_url(url):
    text = get_HTML(url)
    soup = BeautifulSoup(text, "html.parser")  # 解析text中的HTML
    # print(soup)

    content = soup.find_all('div', class_='news-list-content')[0]
    # print(content)

    f = ''
    count = 1
    for fname in content.children:
        fname = str(fname)
        f += (fname.replace("<p>", "").replace("</p>", ""))
        count = count + 1 
        if(count == 9):
            break

    return(f.replace("\n","",1))


url = "http://www.woshipm.com/news"
msg = get_information_from_url(url)
wxURL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d5080997-9eea-4ca2-a0f2-03b128e32a0b'  # 自己
postdata = {'msgtype': 'text', 'text': {'content': msg}}
r = requests.post(wxURL, data=json.dumps(postdata))