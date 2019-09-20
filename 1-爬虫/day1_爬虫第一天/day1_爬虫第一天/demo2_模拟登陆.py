import requests
# data={
#     "ecmsfrom": "",
#     "enews": "login",
#     "tobind": "0",
#     "useraccount": "自己的账号",
#     "password": "自己的密码",
#     "lifetime": "2592000",
# }
# url="https://www.woyaogexing.com/e/member/doaction.php"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Referer":"https://www.woyaogexing.com/e/member/login/" #上一页的链接
}
# 1.
# r=requests.post(url,data=data,headers=headers)
# print(r.text)
# 2.得到登陆成功的cookies
# cookies=r.cookies  # 把得到的cookie保存到一个变量里

# 3. 请求其他页面的时候,把cookies带上
# fav_url="https://www.woyaogexing.com/e/member/fava/?cstr=tx"
# r=requests.get(fav_url,headers=headers,cookies=cookies)
# print(r.text)



# 如果登陆过程过于复杂,没有办法直接模拟,那么可以先在网页上登陆,然后再把 cookies 复制到python里就可以了

# cookies={
    # 写上从 chrome浏览器请求的 request headers 里面的cookie 拿到的数据,转换成字典
# }

# url="http://tpcss.ibeifeng.com/Course/Course"
# r=requests.get(url,cookies=cookies,headers=headers)
# print(r.text)




