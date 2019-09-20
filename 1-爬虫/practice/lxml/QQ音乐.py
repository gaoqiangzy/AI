import requests



# 下载一首歌,可以通过 播放页面的network中找到歌曲的资源链接,然后请求下载,但是只能一次下载一首歌,没有什么意义


url="http://222.73.132.147/amobile.music.tc.qq.com/C4000020VnHM0U9uNh.m4a?guid=397795637&vkey=80DF54F016217CF1A98A0850351955A3BAA7360DF98819ACB77985CC04CC38766967772FA66E0B2BD45D389767CEF2493CA165505B41EDE4&uin=6848&fromtag=66"
# headers={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
#     "Referer":""
# }
# r=requests.get(url,headers=headers,stream=True)
# with open("芒种.mp3",'wb') as file:
#     for j in r.iter_content(10240):
#         file.write(j)


# 想要批量下载资源
# 来自天堂的魔鬼
# http://101.227.216.160/amobile.music.tc.qq.com/C400001DI2Jj3Jqve9.m4a?guid=397795637&vkey=B6EAB8B36B31A8C3410D29AECAFC4F413C4892168F9BC7DA4C94C2FB91C4B5E37D648B62492AAA9BFFE8979346C2CEA131102458E4080C7B&uin=6848&fromtag=66
# 芒种
# http://101.227.216.160/amobile.music.tc.qq.com/C4000020VnHM0U9uNh.m4a?guid=397795637&vkey=80DF54F016217CF1A98A0850351955A3BAA7360DF98819ACB77985CC04CC38766967772FA66E0B2BD45D389767CEF2493CA165505B41EDE4&uin=6848&fromtag=66
# http://101.227.216.160/amobile.music.tc.qq.com/C400003NGKTc2tabpb.m4a?guid=397795637&vkey=22233317B12F23E63C4793E8A3DBA0A80A31AC86FD17FA5FEB13FE02B14B3308F1649D6D37183DE8974CEA1F8B9324EF366D0A261D6A59D5&uin=6848&fromtag=66

# 第一个 ip 地址 # 因为有不同的服务器,换了一下IP还是可以听得,
# 第二个 C400*******.m4a
    # 在列表页的歌曲链接上,发现了和c400 部分相同的字符,但是不全都是一样的,我们假设是,那我们需要找到 所有的歌曲的
    # C400 **??? .m4a 这部分
    # 发现是动态请求,在network中找到了一个musicu.fcg?-=getU 返回的有歌曲的信息
    # 里面有media_mid 和mid 有相同的,有不同的,不同的那部分就是 列表页链接和歌曲资源不同的  name 是歌名
    # 其实mid 是用来放在歌曲链接地址的,然后 media_mid才是歌曲的资源部分
# 第三个 vkey 不同
    # 在列表页全局搜索,没有发现vkey,去播放页面尝试
    # 全局搜索后发现,在一个musicu.fcg?-=getp 链接里返回了vkey 和purl(拼接好完整的路径)
    # 只需要请求该链接就可以获取资源的路径了,但是只能获取一首歌的路径,还是要多请求几首歌,对比不同点
    # https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey1527310703810465&g_tk=5381&loginUin=3004439232&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22397795637%22%2C%22songmid%22%3A%5B%22000P8peU0HhORi%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%223004439232%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%223004439232%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D
    # https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey7741008824760618&g_tk=5381&loginUin=3004439232&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22397795637%22%2C%22songmid%22%3A%5B%22003NGKTc2tabpb%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%223004439232%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%223004439232%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D
    # 不同点 1 getplaysongvkey后面的数字不同,全局搜索后发现是在一个js里面拼接的随机数
    # 不同点 2 songmid  我们在之前取到过 是 mid

# QQ音乐的逻辑
# 1.在列表页面有一个musicu.fcg?-=getU请求,里面含有歌曲的一些信息,包括(歌曲名,歌手名,mid(为了请求vkey的),media_mid(下载音乐时候拼接的))
# 2.在播放页面 会拿着歌曲的mid 请求 purl,得到歌曲的资源路径
# 3. 请求该资源路径,就可以听歌了

