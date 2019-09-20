import  requests,random,time
import json

def get_hot_song_list():
    url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI16992261760781546&g_tk=5381&loginUin=3004439232&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A26%2C%22offset%22%3A0%2C%22num%22%3A100%2C%22period%22%3A%222019_34%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Referer":"https://y.qq.com/n/yqq/toplist/26.html"
    }
    r=requests.get(url,headers=headers)
    resp_dict=json.loads(r.text)
    song_info=[]
    for once in resp_dict['detail']['data']['songInfoList']:
        name=once['name']
        mid=once['mid']
        singer='-'.join(list(map(lambda x:x['name'],once['singer'])))
        song_info.append({'name':name,'mid':mid,'singer':singer})
    return song_info

def get_song_resource(songlist):
    for once in songlist:
        mid=once['mid']
        ran=str(random.random()).replace("0.",'')
        # print(ran)
        url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey"+ran+"&g_tk=5381&loginUin=3004439232&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22397795637%22%2C%22songmid%22%3A%5B%22"+mid+"%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%223004439232%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%223004439232%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
        # print(url)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Referer": "https://y.qq.com/portal/player.html"
        }
        r=requests.get(url,headers=headers)
        resp_dict=json.loads(r.text)
        purl=resp_dict['req_0']['data']['midurlinfo'][0]['purl']
        if purl=="":
            continue
        song_resource="http://isure.stream.qqmusic.qq.com/"+purl
        once['resource']=song_resource
    return songlist

def download(songinfo):
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    }
    for once in songinfo:
        if 'resource' in once:
            audio_r=requests.get(once['resource'],headers=headers,stream=True)
            savePath="./MP3/%s-%s.mp3"%(once['name'],once['singer'])
            # print(savePath)
            with open(savePath,'wb') as file:
                for j in audio_r.iter_content(10240):
                    file.write(j)
            print("%s歌曲下载成功"%(once['name']))



songlist=get_hot_song_list()
# print(songlist)
songinfo=get_song_resource(songlist)
# print(songinfo)
download(songinfo)