import time
import datetime
import requests
import json
import random
import os

wxURL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c623bdfe-a8e4-4d0a-87e1-4e924556e376' #产品群
# wxURL ='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=29d6c6a7-fd67-4e56-91c2-14e0b9c72895' #项目群
# wxURL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d5080997-9eea-4ca2-a0f2-03b128e32a0b'  # 自己
nowTime = datetime.datetime.now()
if datetime.datetime.now().isoweekday() < 6 : # 本程序周末不工作
    if(nowTime.hour < 10):#10点以前运行，提醒早会
        msg = "❤早会时间到了哦！❤"
    else:#10点以后运行，讲笑话
        t = time.time()
        tt = str(random.randint(1400000000, int(t)))  # 随机数 随机获取笑话
        print(tt)
        apiURL = 'http://v.juhe.cn/joke/content/list.php?key=aed468d1b081bf38b3d877208d12dd36&page=1&pagesize=1&sort=asc&time='+tt
        print(apiURL)
        joke = requests.get(apiURL)
        msg = '讲个笑话:'+json.loads(joke.text)['result']['data'][0]['content']
        

    print(msg)
    postdata = {'msgtype': 'text', 'text': {'content': msg}}
    r = requests.post(wxURL, data=json.dumps(postdata))
    print(r.text)
else:
    print("非工作日")
