from glob import glob
from datetime import datetime
from telegram import Bot
import os
import requests
try:ip =requests.get('https://api.ipify.org/').text
except:ip='backup hiddify'
with open(f'{os.path.dirname(__file__)}/token','r')as f:
    token =f.read().split('\n')[0]
print(f"{ip=} {token=}")
files = glob('/opt/hiddify-manager/hiddify-panel/backup/*.json')
os.system("bash /opt/hiddify-manager/hiddify-panel/backup.sh")
files_to_time = [datetime.strptime(i.split('/')[-1].replace('.json','').strip(),"%Y_%m_%d__%H_%M_%S") for i in files]

target = files[files_to_time.index(max(files_to_time))]
if __name__ == "__main__":
    
    chat_id='-1001947065510'
    bot = Bot(token)
    with open(target,'rb') as f:
        bot.send_document(chat_id,f,caption=ip)
    
