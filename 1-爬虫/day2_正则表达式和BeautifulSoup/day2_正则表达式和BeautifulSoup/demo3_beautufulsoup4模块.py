import requests,re
from bs4 import BeautifulSoup

url="http://sh.ziroom.com/z/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Referer":""
}
r=requests.get(url,headers=headers)
# BeautifulSoup(源代码字符串,"解析器") 解析源代码,我们使用的就是 html.parser html解析器
soup=BeautifulSoup(r.text,"html.parser")
# print(soup)
# print(type(soup))

# 查找节点的方式 有两种, 一种是直接 通过 .  soup.head
# 另外一种是使用属性或者函数搜索遍历

# 1.使用 点(.)的方式
# print(soup.head) #查找head标签
# print(soup.head.title) # 查找title标签
# print(soup.head.meta) # 网页中有15个meta标签,但是只会显示出来第一个

# 2.使用遍历文档树,或者搜索的方式
# contents  获取节点的所有子节点  children 返回一个可迭代对象,结果和contents一样,只是需要迭代
# print(soup.head.contents) # 获取head节点的子节点,但是\n 也会被当成是一个节点,下标取值的时候,需要把换行也算在其中
# print(list(soup.head.children))

# descendants 获取标签的所有子孙节点
# print(list(soup.head.descendants))

# parent 当前节点的父节点  parents 当前节点的所有父节点
# print(soup.head.title.parent)

# previous_element  next_element 上一个,下一个节点,
# print(soup.head.next_element.next_element) #会找到 head下的第一个meta
# previous_sibling next sibling 上一个,下一个兄弟节点
# print(soup.head.next_sibling.next_sibling)# 找到 script标签

# find_all(TagName,attrs={"属性名":"属性值",..},text="") 搜索节点
# TagName 标签名,可以是字符串,也可以是列表,也可以是正则
# print(soup.find_all("img")) # 搜索所有的img标签
# print(soup.find_all(['p','span'])) # 同时获取p标签和span标签
# print(soup.find_all(re.compile("h[1-6]"))) # 查找所有满足正则的标签

# print(len(soup.find_all("div")))
# 通过属性查找
# print(soup.find_all("div",attrs={"class":"item"})) # 查找class属性为 item的div
# print(len(soup.find_all("div",attrs={"style":"margin: 0px 21px;"}))) # 发现找不到,去源代码中查看,没有style属性,要以源代码为准

# 通过文本查找 text=
# print(soup.find_all(text="拿铁4.0")) # 找到的只是文本对象,如果想要找标签,需要遍历,使用parent
# print(soup.find_all(text=re.compile("距\d+号线")))

# limit=num 限定查找条数
# print(soup.find_all(text=re.compile("距\d+号线"),limit=2)) # 只查找两条



# 获取文本
# 1.text 获取标签的文本
# print(soup.head.title.text)
# 2.string 获取标签的文本
# print(soup.head.title.string)
# print(soup.find("div",attrs={"class":"tag"}).text) #获取标签下的所有文本,包含子孙标签
# print(soup.find_all("div",attrs={"class":"tag"}).text) # find_all返回的是列表,无法直接使用text
# print(soup.find("div",attrs={"class":"tag"}).string) #string只能获取标签下的文本,而不包含子孙标签



# 获取属性
# attrs 获取该标签下的所有属性,放在一个字典里
for once in soup.find_all('img'):
    try:
        print(once.attrs['src'])
    except KeyError:
        pass