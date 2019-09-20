import re,requests
from bs4 import BeautifulSoup


def get_page_info(page=1):
    url="https://www.danke.com/room/sh?page="+str(page)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Referer":"https://www.danke.com/sh"
    }
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    house_list=soup.find_all("div",attrs={"class":"r_lbx"})
    for once in house_list:
        house_name=once.find("div",attrs={"class":"r_lbx_cena"}).a.attrs['title']
        house_url=once.find("div",attrs={"class":"r_lbx_cena"}).a.attrs['href']
        house_price=once.find("span",attrs={"class":"ty_b"}).text.strip()
        house_station_info=once.find("div",attrs={"class","sub_img"}).next_element.strip()
        house_info4=once.find(text=re.compile("㎡"))
        house_info4=re.sub("\s",'',house_info4)
        try:
            house_discount=once.find("div",attrs={"class":"new-price-link"}).text
            house_discount=re.sub("\s",'',house_discount)[:-2]
        except AttributeError :
            house_discount="暂无优惠"
        print(house_discount)

for page in range(1,5):
    get_page_info(page)


# import re
#
# str1="距5号环中线,10号线五和站400米"
# str2="距3号龙岗线六约站250米"
# str3="距1号罗宝线,3号龙岗线购物公园站850米"
# str4="距2号蛇口线,9号线景田站500米"
# str5="距9号线香梅站200米"
# regex="距(?:(\d+)号([\u4e00-\u9fa5]*)线,)?(\d+)号([\u4e00-\u9fa5]*)线([\u4e00-\u9fa5]*)站(\d+)米"
# print(re.search(regex,str1).groups())
# print(re.search(regex,str2).groups())
# print(re.search(regex,str3).groups())
# print(re.search(regex,str4).groups())
# print(re.search(regex,str5).groups())
