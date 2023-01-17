import requests,re
from bs4 import BeautifulSoup

def get_page_info(page=1):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer":"https://www.danke.com/recommend-list/bj?rent_type=entire_rent",
        "Cookies":"sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ccb9cb8d382a-04860803174b96-3c375f0d-2073600-16ccb9cb8d4813%22%2C%22%24device_id%22%3A%2216ccb9cb8d382a-04860803174b96-3c375f0d-2073600-16ccb9cb8d4813%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.baimin.com%2Fbaimin%2Fgo.aspx%3Flink%3Dhttp%253a%252f%252fwww.dankegongyu.com%22%2C%22%24latest_referrer_host%22%3A%22www.baimin.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22platformType%22%3A%22PC%22%2C%22pid%22%3A%22dankegongyu_customer%22%2C%22cid%22%3A%22bj%22%2C%22ucid%22%3A%22%22%2C%22uuid%22%3A%22%22%2C%22ssid%22%3A%22%22%2C%22lmei%22%3A%22%22%2C%22android_id%22%3A%22%22%2C%22idfa%22%3A%22%22%2C%22idfv%22%3A%22%22%2C%22mac_id%22%3A%22%22%7D%7D; UM_distinctid=16ccb9d706815b-0d57405da609f2-3c375f0d-1fa400-16ccb9d7069224; CNZZDATA1271579284=2132158339-1566781231-https%253A%252F%252Fwww.danke.com%252F%7C1566781231; Hm_lvt_814ef98ed9fc41dfe57d70d8a496561d=1566784195; Hm_lpvt_814ef98ed9fc41dfe57d70d8a496561d=1566784209; XSRF-TOKEN=eyJpdiI6Im1vOGdYa1JYUnU0TmdFM2VvbVBWZnc9PSIsInZhbHVlIjoiK1cxYzFmNFFRcnVlcEhFMmR4VVBYcllJSUx3UkR5Q3FvZnRIYVBrRVJZOFNuQytjSmRKUFlyZjREN1k0UXk0ME53Z0hQTlJlbzM2TFRXVHBtMEIrV0E9PSIsIm1hYyI6ImUwYjRmNjcwYWUxZThmMDI4N2M2ZmY1Mjc4NWM5NzQ0MzhmNjNkOWM3MTMzYTA2ODZkYTI0Yzg4YWY5MmMxNWMifQ%3D%3D; session=eyJpdiI6IkhIcDF4blVJSUZrNDhIN1RCU2VWSFE9PSIsInZhbHVlIjoiYWVBRDF4eFRQa2gydU1Cd0d2VFduN2NGZ0FnNHVIOFVRWGw3ZVVoQTc0bTMxWUFKVjZwSnBya0pLb1k4OUpcL0hKNFFuVHFHNWlGTGlBK0YycEdvQmZRPT0iLCJtYWMiOiJmMjEwNDZlOWQyMzA2YTE2YmEzZDYzMDRhYzQyMmUyN2QxN2EzM2IyYzhjZjYyOTI2NzYxOGQ3ZDU4NGFkNDJjIn0%3D"
    }
    # 请求链接获取网页源代码
    r=requests.get(f"https://www.danke.com/room/bj/c%E6%95%B4%E7%A7%9F.html?from=all&page={page}",headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")

    # 1.爬取所有包含房源信息的div
    all_div = soup.find_all('div',attrs={"class":"r_lbx"})
    page_info=[]
    # 遍历div,然后从每个中查找想要的内容 (房源的名称,房源的url,房源的平方数,楼层,几号线,地铁站,米数,金额)
    for once in all_div:
        try:
            # 1.获取图片地址
            img_url = once.find("img", attrs={"alt": "图片"}).attrs["src"]
            # 2.获取房源名称
            title = once.find("div",attrs={"class":"r_lbx_cena"}).a.text.strip()
            # 3.获取房源url
            house_url=once.find("div",attrs={"class":"r_lbx_cena"}).a.attrs["href"]
            # 4.获取房源平方数
            infos=once.find("div",attrs={"class":"r_lbx_cenb"}).text.strip()
            house_square=infos.split("|")[0].strip()
            house_floor=infos.split("|")[1].strip()
            # 获取车站信息
            station_info=once.find("div",attrs={"class","r_lbx_cena"}).div.text.strip()
            # print(station_info)
            result=re.search("距(.*)线(.*?)站(\d{1,4})米",station_info).groups()
            print(result)
            line = result[0]+"线"
            station = result[1]+"站".strip()
            meters = result[2]+"米".strip()
            page_info.append({"title":title,"house_url":house_url,"house_square":house_square,"house_floor":house_floor,"line":line,"station":station,"meters":meters,"img_url":img_url,"headers":headers})
            # print(page_info)
        except AttributeError as e:
            print(e)
            print(page_info)
    return page_info

# 保存信息到本地文件
def save_info_to_file(infos):
    with open("蛋壳公寓房源.csv","a",encoding="utf-8") as file:
        for info in infos:
            print(info['line'])
            file.write("%s,%s,%s,%s,%s,%s,%s,%s\n"%(info['title'],info['house_url'],info['house_square'],
                                                    info['house_floor'],info['line'],info['station'],info['meters'],info['img_url']))

# 保存图片到本地
def save_img_to_file(imgs):
    for img in imgs:
        flag_https = img['img_url'].find("https")
        if(flag_https !=-1):
            try:
                img_r=requests.get(img['img_url'],headers=img['headers'],stream=True)
                with open("./images/%s.jpg"%(img['title'][0:3]),"wb") as file:
                    for i in img_r.iter_content(10240):
                        file.write(i)
                print(f"{img['title']}图片下载成功")
            except Exception as e:
                print(e)
for page in range(1,13):
    infos= get_page_info(page)
    save_info_to_file(infos)
    save_img_to_file(infos)
    print(f"第{page}页信息加载成功,本页保存了{len(infos)}条信息")

# get_page_info()
