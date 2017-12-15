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