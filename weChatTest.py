import time
import datetime
import requests
import json
import random
import os


if datetime.datetime.now().isoweekday() < 6 : # 本程序周末不工作
     
    t = time.time()
    tt = str(random.randint(1400000000, int(t))) #随机数 随机获取笑话
    print(tt)
    apiURL = 'http://v.juhe.cn/joke/content/list.php?key=aed468d1b081bf38b3d877208d12dd36&page=1&pagesize=1&sort=asc&time='+tt
    print(apiURL)
    msg = requests.get(apiURL)
    joke = '讲个冷笑话:'+json.loads(msg.text)['result']['data'][0]['content']
    print(joke)

    

    

    #wxURL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d5080997-9eea-4ca2-a0f2-03b128e32a0b' #产品群
    #wxURL ='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=29d6c6a7-fd67-4e56-91c2-14e0b9c72895' #项目群
    wxURL ='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ff77580c-a5f5-47d7-b1e4-a76342523a73' # 自己
    postdata = {'msgtype': 'text', 'text': {'content': joke}}
    r = requests.post(
    wxURL, data=json.dumps(postdata))
    print(r.text)