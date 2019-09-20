import requests,re
from lxml import etree
# 爬取豆瓣电影top排名
# 图片路径,电影名,演员和导演,年份,国家,类别,评分,人数,简介
page=2
url="https://movie.douban.com/top250?start="+str((page-1)*25)+"&filter="
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer":"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=11&tn=98012088_5_dg&bar=&wd=top250&oq=%25E7%25B3%2597%25E4%25BA%258B%25E7%2599%25BE%25E7%25A7%2591&rsv_pq=e4cf98880002fbc8&rsv_t=641cGlbKKIWtbU8hyrB4%2BbcABgH93eMlc8SpxvF0FZTUBo20u3H18lTTphV2R6HWG3YERw&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=57629"
}
r=requests.get(url,headers=headers)
# print(r.text)
html=etree.HTML(r.text)
movie_list=html.xpath("//ol[@class='grid_view']/li")
for once in movie_list:
    img_url=once.xpath("./div/div[1]/a/img/@src")[0]
    title=once.xpath("./div/div[2]/div[1]/a/span[1]/text()")[0]
    director=once.xpath(".//div[@class='bd']/p[1]/text()")[0].strip()
    try:
        director=re.search("导演: (.*?)主(?:演: (.*?)...)?",director).groups()
    except BaseException:
        # print(title)
        pass
    info=once.xpath(".//div[@class='bd']/p[1]/text()")[1].split("/")
    year=info[0].strip()
    country=info[1].strip()
    type=info[2].strip()

    # print(year,country,type)
    score=once.xpath(".//span[@class='rating_num']/text()")[0]
    comment_num=once.xpath(".//div[@class='star']/span[last()]/text()")[0][:-3]
    intro=''.join(once.xpath(".//span[@class='inq']/text()"))
    print(title)

#  1   0
#  2   25
#  3   50
#  4   75
# (page-1)*25