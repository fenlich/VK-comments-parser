import requests
import time
from datetime import datetime
TOKEN_USER = #write here your token
VERSION = '5.131' #write here the current version of VK API
DOMAIN = #write here a domain of the group
response = requests.get('https://api.vk.com/method/wall.get',
params={'access_token': TOKEN_USER,
        'v': VERSION,
        'domain': DOMAIN,
        'count': 100,
        'filter': str('owner')})
data = response.json()['response']['items']
id_1 = []
for post in data:
        id_1.append(post['id'])  
text = [] 
date_unix = []   
for j in range(0, 101, 100):
    print(j)
    for k in id_1:       
        response2 = requests.get('https://api.vk.com/method/wall.getComments',
        params={'access_token': TOKEN_USER,
        'v': VERSION,
        'count': 100,
        # 'offset': j,
        'owner_id': #write the id of the group with a minus,
        'post_id': k})

        response2.json()
        r = response2.json()
        size = len(r.get('response').get('items'))
    
        for i in range(0, size):
            if len(r.get('response').get('items')[i].get('text')) != 0:
                text.append(r.get('response').get('items')[i].get('text'))
                date_unix.append(r.get('response').get('items')[i].get('date'))
        time.sleep(0.15)
 
with open("texts.txt", "wt", encoding = "utf8") as f:
    for t in text:
        f.write(t.replace("\n", " ") + "\n")
date = []
for i in date_unix:
    date.append(datetime.utcfromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S'))
