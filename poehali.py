import requests

data = '[[0,500],[5,500],[18,100],[30,115],[50,50],[80,35],[130,18],[190,20],[200,0]]'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.37'
headers = {'Origin': 'http://jetbrains.ru', 'Accept': '*/*', 'Referer': 'http://jetbrains.ru/poehali/', 'User-Agent': ua}
response = requests.post(url='http://rckt.jetbrains.com/compute.jsp', headers=headers, data=data)
try :
    result = response.json()
    for i in result['waypoints']:
        print i
    print result['position'], result['score'], result['state']
except:
    print response.text