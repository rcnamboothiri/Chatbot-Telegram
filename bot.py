
# import time
# import json
# import random
# import datetime
# import requests
# import schedule
# import telepot
# from telepot.loop import MessageLoop


# # def randomtemperature():
# #  random.seed()
# #  return str(round(random.uniform(50, 100),2))

# # def currenttime():
# # 	now = datetime.datetime.now() - datetime.timedelta(hours = 5) - datetime.timedelta(minutes = 30)
# # 	formatted_time = "{0}T{1}Z".format(now.date(),now.time())

# # 	return formatted_time


# # def schedule_job():
# # 	payload = []
# # 	print(json.dumps(payload))
# # 	r = requests.post("https://api.telegram.org/502645220:AAGrmzWcIE4VLY_FczaVNIjvZciZb5g1_2I/getMe", data= json.dumps(payload))
# # 	print(r.status_code)
# # 	print(r.content)



# # schedule.every(5).seconds.do(schedule_job)
# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)



# token = '502645220:AAGrmzWcIE4VLY_FczaVNIjvZciZb5g1_2I'
# TelegramBot = telepot.Bot(token)
# # print(TelegramBot.getMe())
# f = open('log.txt', 'r')
# print(f.read())
# last_entry = f.read() 
# print(json.dumps(TelegramBot.getUpdates(offset=210122043)))


import sys
import time
import telepot
from telepot.loop import MessageLoop
from time import gmtime, strftime
import datetime


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text' and msg['text'].lower()=='time' :
	        	bot.sendMessage(chat_id,currenttime())
    else:
    	bot.sendMessage(chat_id,"Sorry,I didn't get you.I am still in learning phase..!!!")
       
def currenttime():
	now = datetime.datetime.now() 
	formatted_time = "{0}".format(now.time())
	return formatted_time


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)