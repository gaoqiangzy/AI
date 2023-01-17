import requests,re,time
from lxml import etree


house_id=set() # 用来检测去重

def get_page_info(page=1):
    url="https://shanghai.anjuke.com/sale/p"+str(page)+"/#filtersort"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Referer":"https://shanghai.anjuke.com/"
    }

    r=requests.get(url,headers=headers)
    # print(r.text)
    html=etree.HTML(r.text)
    house_list=html.xpath("//li[@class='list-item']")
    house_info=[]
    for once in house_list:
        url=''.join(once.xpath(".//a[@class='houseListTitle ']/@href"))
        id = re.search("A(\d+)\?", url).group(1)
        if id in house_id:
            continue
        else:
            house_id.add(id)

        title=''.join(once.xpath(".//a[@class='houseListTitle ']/@title"))
        infos=once.xpath(".//div[@class='details-item']/span/text()")
        household=infos[0]
        square=infos[1].strip()[:-2]
        floor=infos[2]
        year=infos[3].strip()[:-3]
        infos2=''.join(once.xpath(".//span[@class='comm-address']/@title"))
        infos2=re.search("(.*?)\s+(.*?)-(.*?)-(.*)",infos2).groups()
        village=infos2[0]
        area=infos2[1]
        middle_area=infos2[2]
        position=infos2[3]
        price=''.join(once.xpath(".//span[@class='price-det']/strong/text()"))
        unit_price=''.join(once.xpath(".//span[@class='unit-price']/text()"))[:-4]
        house_info.append({
            "url":url,
            "id":id,
            "title":title,
            "household":household,
            "square":square,
            "floor":floor,
            "year":year,
            "village":village,
            "area":area,
            "middle_area":middle_area,
            "position":position,
            "price":price,
            "unit_price":unit_price,
        })
    return house_info


def saveToCsv(house_info):
    with open("安居客房源信息.csv",'a',encoding='utf-8') as file:
        for once in house_info:
            file.write('::'.join(list(once.values()))+"\n")


for page in range(3,50):
    house_info=get_page_info(page)
    saveToCsv(house_info)
    print("%d页数据下载成功"%(page))
    time.sleep(3)