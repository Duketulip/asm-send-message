# -*- coding:utf8 -*-
import time
import datetime
import schedule
import sendWxMsg
 

 
    


#计划任务
 
#schedule.every().day.at("18:00").do(sendWxMsg.send())
schedule.every(1).minutes.do(sendWxMsg.send)
while True:
    schedule.run_pending()
    time.sleep(3)