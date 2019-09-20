import requests
from lxml import etree

html_str=open("index.html",'r',encoding='utf-8').read()
# print(html_str)
# 使用lxml解析html源代码
html=etree.HTML(html_str) # soup=BeautifulSoup(r.text,"html.parser")
# print(html) # <Element html at 0x1db33b459c8>
# 想要查看 节点的源代码,使用etree.tostring(节点对象)
# print(etree.tostring(html,encoding='utf-8').decode("utf-8"))

# xpath('xpath规则') 返回的是列表形式,如果没有查到就是空列表

# nodename 查找某个节点,
# print(html.xpath("head")) # 查找html下的head节点
# print(html.xpath("body")) # 查找html下的body节点

# / 放在开头代表从根节点选取  element/element 如果放在节点后面代表节点的下一层节点
# print(html.xpath("/html/head")) # 查找根节点下的html下的head节点
# print(html.xpath("head/title")) #查找head下面的title节点
# print(html.xpath("body/div")) # 取到body下的div,有几个显示几个,bs4只能显示第一个
# print(html.xpath("body/div")[1].xpath('ul/li')) # 取到div下标为1的,再去查找ul下的li

# // 搜索,不考虑层级查找标签
# print(html.xpath("//li")) #查找所有的li标签
# print(html.xpath("//li/text()")) #查找所有的li标签下的文本
# print(html.xpath("body/div/ul/li")) # 查找div下的ul下的li标签,如果层级不符合,则不匹配
# print(html.xpath("body/div//li")) # 在满足条件的div中搜索li标签

# . 从当前节点开始查询
# 查找所有的房源的名称和平方数
# 1.查找所有class为nav的div
# all_house=html.xpath("//div[@class='list']") # 查找class为nav的div  soup.find_all("div",attrs={"class":"list"})
# print(all_house)
# for once in all_house:
#     # print(once.xpath("//li/text()")) # 需要注意的是 此处的// 不会考虑是从哪个节点xpath的,而是查找的源代码中的 li标签
#     print(once.xpath(".//li/text()")) # 加上. 代表从当前节点也就是once部分查找所有的li

# ..  从当前节点的上一层节点开始查询


#  [@attr=value] 属性名=属性值  #查找的是属性名= 该属性值的,而不是像bs4那样,包含关系
#  使用 contains(@属性名,"属性值") 处理包含关系
# print(html.xpath("//div[@class='content']")) #class属性= content的
# print(html.xpath("//div[@class='content clearfix']"))#class属性= content clearfix的
# print(html.xpath("//div[contains(@class,'content')]")) # 查找class属性包含 content字符的


# 谓语部分
# print(html.xpath("body/div")[1].xpath('ul/li/text()'))
# [num] 代表取该元素下的第num位,但是是从1开始计数的
# print(html.xpath('body/div[2]//li/text()'))
# print(html.xpath("//li[2]/text()")) # num 计数是按照同一层级计数的
# print(html.xpath("//li/text()")[1]) # 如果想要得到所有li的第二个,使用列表下标的方式

# print(html.xpath("//div[@class='inner']//li[last()]/text()")) #last() 代表最后一个
# print(html.xpath("//div[@class='inner']//li[last()-1]/text()")) #last() 代表倒数第二个

# print(html.xpath("//div[@class='inner']//li[position()>3]/text()")) # 找到位置大于3的
# print(html.xpath("//div[@class='inner']//li[position()>2 and position()<5]/text()")) # 找到位置大于3的小于5
# print(html.xpath("//div[@class='inner']//li[position()=2 or position()=5]/text()")) # 找到位置等于5或者等于3的

# *通配符 选取位置节点
# print(html.xpath("//li[@data-id]/text()")) #查找带有 data-id 属性的li标签的文本
# print(html.xpath("//li[@*='4']/text()")) # 查找属性值为4的li标签
# print(html.xpath("//*[@*='4']/text()")) # 查找属性值为4的任意标签
# print(html.xpath("head/node()")) # 查找head节点下的所有子节点,类似 bs4的contents


# | 或者关系 ,合并结果集
# print(html.xpath("//span/text() | //li/text()")) # 合并所有span的文本和li的文本


# 文本
# text() 只能取标签下的文本
# print(html.xpath("//div[@class='inner']/ul/text()"))
# print(''.join(html.xpath("//div[@class='inner']/ul//text()"))) # 使用 // text() 获取该节点下的所有层级的文本,然后再用 合并 join() 可以达到和string一样的效果
# string() 写法特别, 可以取到标签下的所有文本,并且返回的不再是列表,而是字符串
# print(html.xpath("string(//div[@class='inner']/ul)"))

# 属性
# 在标签下面 使用  /@属性名 即可得到改标签的属性
# print(html.xpath("//span[@class='txt']/@data-sid")) #
# print(html.xpath("//img/@src")) # 获取所有图片标签的路径