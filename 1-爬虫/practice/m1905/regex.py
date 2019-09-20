import requests,re

def getPageInfo(pageindex=1):
    url = "https://www.1905.com/vod/list/n_1/o3p"+str(pageindex)+".html"
    # "https: // www.1905.com / vod / list / n_1 / o3p2.html"
    # "https: // www.1905.com / vod / list / n_1 / o3p3.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"

    }
    r = requests.get(url, headers=headers)
    html = r.content.decode("utf8")
    div_regex = '<div class="grid-2x grid-3x-md grid-6x-sm">(.*?)</div>'
    div_list = re.findall(div_regex, html, re.DOTALL)
    PageInfo = []
    for div in div_list:
        href_regex = '<a class="pic-pack-outer" target="_blank" href="(.*?)" title="(.*?)">'
        href = re.search(href_regex, div).group(1)
        title = re.search(href_regex, div).group(2)
        img_regex = '<img alt="(.*?)" src="(.*?)">'
        img = re.search(img_regex, div).group(2)
        try:
            score_regex = '<i class="score"><b>(.*?)</b>(.*?)</i>'
            score = re.search(score_regex, div).group(1) + re.search(score_regex, div).group(2)
        except AttributeError as e:
            score=''
        introduce=re.search('<p>(.*?)</p>',div,re.DOTALL).group(1)
        PageInfo.append({"title": title, "href": href, "img": img, "score": score, "introduce": introduce})
    return PageInfo

def SaveFile(pageInfo):
    with open('电影.csv','a',encoding='utf-8') as file:
        # file.write('%s,%s,%s,%s,%s\n'%('电影名','链接地址','图片','评分','简介'))
        for i in pageInfo:
            file.write('%s,%s,%s,%s,%s\n'%(i['title'],i['href'],i['img'],i['score'],i['introduce']))
def SaveImg(pageInfo):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    img_url=pageInfo['img']
    title = pageInfo['title']
    img_r = requests.get(img_url,headers=headers,stream=True)
    with open('./imgs/%s.jpg'%(title),'wb') as file:
        for i in img_r.iter_content(10240):
            file.write(i)
for page in range(1,99):
    pageInfo=getPageInfo(page)
    SaveFile(pageInfo)
    SaveImg(page)
    print(f"第{page}页信息加载成功，保存了{len(pageInfo)}条信息")