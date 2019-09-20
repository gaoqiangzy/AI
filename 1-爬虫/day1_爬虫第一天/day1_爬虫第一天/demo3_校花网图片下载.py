import requests,re


url="http://www.xiaohuar.com/hua/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Referer":"http://www.xiaohuar.com/"
}
r=requests.get(url,headers=headers)
html=r.text
# print(html[10000:10100]) # 切片方式太慢了,不可取
# 对比 多个img标签的规律
# <img width="210"  alt="华东师范大学校花底泽毅" src="/d/file/20190823/a110ceb73ca709dfa405064489350ba8.jpg" />
# <img width="210"  alt="上海民航职业技术学院校花蒋云琪" src="/d/file/20190823/75149a1f9845c50e8158c64793be8759.jpg" />
# <img width="210"  alt="厦门理工学院校花窦梦诗" src="/d/file/20190822/3549081976df334fdd11b6ee53523e34.jpg" />
# <img width="210"  alt="广东海洋大学 校花李微儿" src="/d/file/20190819/small2daa4b57381c18655ad759e45c9f648f1566179840.jpg" />

# 两个不同点
# 1. alt 属性
# 2. src 属性

# 正则表达式
img_regex='<img width="210"  alt="(.*?)" src="(.*?)" />'
result=re.findall(img_regex,html)
result=list(map(lambda x:[x[0],"http://www.xiaohuar.com"+x[1]],result))
for once in result:
    print(once)
    # img_r=requests.get(once[1],headers=headers,stream=True)
    # with open("./images/%s.jpg"%(once[0]),'wb') as file:
    #     for j in img_r.iter_content(10240):
    #         file.write(j)
    # print("%s图片下载成功"%(once[0]))
