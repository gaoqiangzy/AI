from lxml import  etree

html_str=open("index.html","r",encoding="utf-8").read()
html=etree.HTML(html_str)
header=html.xpath('//div[@class="header"]/text()')[0]

print(html.xpath('//div[@class="header"]/@price')[0])

print(html.xpath('/html/head/title'))
print(html.xpath('/html/body/div/div')[0].text)

print(html.xpath('//div[@class="rightBody"]//li')[1].text)
rightBody_li=html.xpath('//div[@class="rightBody"]//li')
for li in rightBody_li:
    print(li.text)
    print(li.xpath('./@name'))

leftBody=html.xpath('//div[@class="leftBody"]//li[2]')
print(leftBody[0].text)

leftBody2=html.xpath('//div[@class="leftBody"]//li[2]/text()')[0]
print(leftBody2)

list = [ '1','2','','abc']
a='x'.join(list)
print(a)