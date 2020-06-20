 
import time
import requests
import json
import random
import os

print(123)
def send():
    print(123)
    os.system('cls')    
    t = time.time()
    time_local = time.localtime(t)  # 转换为win_time
    dt = time.strftime("%H:%M", time_local)  # 转换成新的时间格式(18:59)
    
    print(dt)
 
    if dt != '18:00':
        return
    else:
        tt = str(random.randint(1400000000, int(t)))
        print(tt)
        apiURL = 'http://v.juhe.cn/joke/content/list.php?key=aed468d1b081bf38b3d877208d12dd36&page=1&pagesize=1&sort=asc&time='+tt
        print(apiURL)
        msg = requests.get(apiURL)
        joke = '讲个冷笑话:'+json.loads(msg.text)['result']['data'][0]['content']
        print(joke)

        # 下面替换成您的数据
        # wxURL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c623bdfe-a8e4-4d0a-87e1-4e924556e376'产品群
        wxURL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d5080997-9eea-4ca2-a0f2-03b128e32a0b'
        postdata = {'msgtype': 'text', 'text': {'content': joke}}
        r = requests.post(
            wxURL, data=json.dumps(postdata))
        print(r.text)
send()
