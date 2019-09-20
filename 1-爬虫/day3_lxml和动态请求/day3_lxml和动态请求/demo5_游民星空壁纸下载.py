# http://pic.gamersky.com/bz/
# 下载该网页中所有的壁纸

import requests,json


url="http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=1&pageSize=50&nodeId=21089"
url="http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=2&pageSize=50&nodeId=21089"
url="http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=3&pageSize=50&nodeId=21089"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer":"http://pic.gamersky.com/bz/"
}
r=requests.get(url,headers=headers)
resp_dict=json.loads(json.loads(r.text))
# print(resp_dict)
# print(type(resp_dict))
for once in resp_dict['body']:
    img_url=once['originImg']
    img_name=once['title']
    print(img_name,img_url)