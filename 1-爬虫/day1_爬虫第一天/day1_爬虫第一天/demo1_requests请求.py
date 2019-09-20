import requests


# 网址
# url="http://www.antvv.com"
# url="https://www.woyaogexing.com"
# r=requests.get(url)
# print(r)  #<Response [200]> 返回值对象,返回了一个http状态码
# print(type(r))

# text 获取返回值的源代码,如果误判了编码会乱码
# print(r.text)

# status_code 返回的状态码
# print(r.status_code)

# encoding 网页的编码,可能会误判
# print(r.encoding)


# r.content  返回源代码的字节码,不做解析 , decode(编码类型) 把字节码转换为指定的编码
# print(r.content.decode("utf-8"))


# 尝试请求知乎
# url="https://www.zhihu.com"
# url="http://httpbin.org/get"
# r=requests.get(url) # 直接请求知乎失败,得到400 错误,因为知乎做了UA(User-Agent)判断
# 请求 测试网站,发现 UA 是 python-requests/2.18.4,知乎发现了我们是使用爬虫访问的,所以限制了我们,我们需要自己设定UA访问
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }
# r=requests.get(url,headers=headers) # 加上UA了之后就可以访问了
# print(r.text)



# json 字符串处理
# url="http://httpbin.org/get"
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }
# r=requests.get(url,headers=headers) # 加上UA了之后就可以访问了
# json_str=r.text # 返回的类似 字典或者列表的字符串,但是是 str类型, 我们叫它 json字符串 ,是一种数据交换格式,各个语言都有解析json的方式
# print(r.text['origin'])
# print(type(r.text))
# 引入python的json模块,可以解析 json字符串
import json
# json.loads() 是把 json字符串转换成  python对象
# json_dict=json.loads(json_str)
# json_dict=r.json() # requests模块自带的json解析
# print(json_dict)
# print(type(json_dict))
# print(json_dict['origin'])


# 获取原始内容 stream=True 流式传输
# url="http://www.xiaohuar.com/d/file/20190822/3549081976df334fdd11b6ee53523e34.jpg"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
# r=requests.get(url,headers=headers)
# print(r.text) # 会解析成乱码,因为是一张图片,没有办法通过文本的方式解析
# print(r.content) # 返回原始内容,但是是一次性把整个文件下载下来,如果遇到了大文件,就不好处理了
# 在请求的时候加上 stream= True
# r=requests.get(url,headers=headers,stream=True)
# 读取的时候 使用 r.iter_content(num) 每次读取num字节
# with open("xiaohuar1.jpg",'wb') as file:
#     for j in r.iter_content(10240): #每次读取10240字节= 10kb 写入到文件中
#         file.write(j)

# # 下载音频
# url="https://m10.music.126.net/20190824144952/faa8f0ca7ae422e8866afadfa3aa62d5/ymusic/0f53/510b/0709/895a49dd17fa7ae02f850c1b4d4df12e.mp3"
# r=requests.get(url,headers=headers,stream=True)
# with open("孤身.mp3",'wb') as file:
#     for j in r.iter_content(10240):
#         file.write(j)


# get 方式传递参数
# 1.直接拼接在url后方
# url="http://www.antvv.com/?cate=3"
# 2.使用params 参数
# url="http://www.antvv.com"
# params={
#     "cate":"2"
# }
# r=requests.get(url,params=params)
# print(r.text)


# timeout=float   设置超时秒数,如果超过了设定时间,服务器没有返回内容,则报错
# url="https://www.zhihu.com"
# try:
#     r=requests.get(url,timeout=0.1)
# except BaseException:
#     print("超时了,")
# else:
#     print(r.text)


# proxies={} 设置代理
# url="http://httpbin.org/get"
# proxies={
#     "http":"183.166.138.176:808"
# }
# r=requests.get(url,proxies=proxies)
# print(r.text) # 101.80.14.201 成功后,发现服务器检测到的ip是183.166.138.176


# 网站请求post接口
# http://httpbin.org/post
url="http://httpbin.org/post"
# data 向服务器发送表单数据,一般做模拟登录使用
data={
    "username":"admin1234",
    "password":"888888"
}
# files 向服务器发送文件
files={
    # "img":open("xiaohuar.jpg",'rb')
    "html":open("index.html",'rb')
}
# data 向服务器发送json字符串,只需要把data使用json.dumps()转换一下即可

r=requests.post(url,data=data,files=files)
print(r.text)
