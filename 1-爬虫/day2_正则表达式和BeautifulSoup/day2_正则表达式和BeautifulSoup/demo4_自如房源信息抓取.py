import requests,re,time
from bs4 import BeautifulSoup


def get_page_info(page=1):
    url="http://sh.ziroom.com/z/p"+str(page)+"/"
    # url='http://sh.ziroom.com/z/p2/'
    # url="http://sh.ziroom.com/z/p3/"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer":""
    }
    # print(url)
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")

    # 先爬取所有的div,每个div中包含房源的信息
    all_div=soup.find_all("div",attrs={"class":"item"})
    # print(all_div)
    # 遍历30个div,然后从每个中查找想要的内容 (房源的名称,房源的url,房源的平方数,楼层,几号线,地铁站,米数,金额)
    page_info=[]
    for once in all_div:
        try:
            title=once.find("h5",attrs={"class":"title"}).a.text
            url="http:"+once.find("h5",attrs={"class":"title"}).a.attrs['href']
            infos=once.find(text=re.compile("㎡"))
            square=infos.split("|")[0][:-2]
            floor=infos.split("|")[-1]
            station_info=once.find("div",attrs={"class":"location"}).text.strip()
            result=re.search("小区距(\d{1,2})号线(.*?)站步行约(\d{1,4})米",station_info).groups()
            line=result[0]
            station=result[1]
            meter=result[-1]
            page_info.append({"title":title,"url":url,"square":square,"floor":floor,"line":line,"station":station,"meter":meter})
        except AttributeError as e:
            print(once)
            print(e)
    return page_info

def save_to_file(infos):
    with open("自如房源.csv",'a',encoding='utf-8') as file:
        for once in infos:
            file.write("%s,%s,%s,%s,%s,%s,%s\n"%(once['title'],once['url'],once['square'],once['floor'],once['line'],once['station'],once['meter']))

for page in range(1,51):
    infos=get_page_info(page)
    save_to_file(infos)
    print("第%d页信息加载成功,本页保存了%d条信息"%(page,len(infos)))
    # time.sleep(2)


