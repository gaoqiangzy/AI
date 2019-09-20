import re


# phone_str="18616261234"
# complie() 编译正则表达式,得到一个正则表达式对象
# phone_regex=re.compile("^1[3-9](\d{9})$")
# print(phone_regex)
# print(type(phone_regex))

# match() 从字符串的开头开始匹配,匹配成功则结束,返回一个match对象,如果匹配失败,返回None值
# result=phone_regex.match(phone_str)
# group(num) 获取match对象中某一个分组,如果没有指定分组,那么就返回所有匹配到的内容
# print(result.group()) # 查找所有匹配到的内容
# print(result.group(1))  # 查找匹配到的第一个分组


# 直接匹配
# result=re.match("^1[3-9](\d{9})$",phone_str)
# print(result.group())


# search() 从字符串的任意位置开始匹配,其他的跟match相同
# person_info="我是tom,我的手机号是 18616261234.我还有一个手机号是 13613948574."
# result=re.match("^1[3-9](\d{9})$",person_info)
# result=re.search("1[3-9](\d{9})",person_info)
# print(result)
# print(result.group())

# findall() 从字符串中匹配所有满足条件的字符,如果正则里面包含分组,那么会返回分组里面的内容
# person_info="我是tom,我的手机号是 18616261234.我还有一个手机号是 13613948574."
# result=re.findall("1[3-9](\d{9})",person_info) #['616261234', '613948574']
# result=re.findall("1[3-9]\d{9}",person_info) #['18616261234', '13613948574']
# 出现了括号,但是又不想当成是分组的时候, 在分组的开始括号后面加上一个 ?:  比如 (?:\d+)
# result=re.findall("1[3-9](?:\d{9})",person_info)
# 如果有多个分组,那么多个分组的值,会以元组的形式返回
# result=re.findall("(1[3-9]\d)(\d{4})(\d{4})",person_info) # [('186', '1626', '1234'), ('136', '1394', '8574')]
# print(result)


# finditer() 使用方法等同于findall() 只是返回值是一个可迭代对象
# person_info="我是tom,我的手机号是 18616261234.我还有一个手机号是 13613948574."
# result=re.finditer("(1[3-9]\d)(\d{4})(\d{4})",person_info)
# print(result)
# for once in result:
#     # print(once.group(2))
#     print(once.groups()) # groups() 取到所有的分组


# python分割字符串 str.split("")
# str1="唱,跳_rap,篮球"
# print(str1.split("_"))
# re.split()  使用正则表达式分割
# print(re.split(",|_",str1))
# print(re.split("[,_]",str1))


# sub(正则,要替换成什么,字符串,指定替换的次数)  subn() 返回替换过后字符的同时,返回替换的次数
# filepath="a>b<c?a:b\"*\\/|.txt"
# filepath=filepath.replace(">","").replace('<','').replace(":","").replace("?","")
# filepath=re.sub("[>\\\\<\?\*:\"/\|]","",filepath)
# filepath=re.subn("[>\\\\<\?\*:\"/\|]","",filepath,2)
# print(filepath)
# with open(filepath,'w',encoding='utf-8') as file:
#     file.write("hello world")


# 引用分组
# phone="18616261234"
# print(re.sub("(1[3-9]\d)(\d{4})(\d{4})","\\1****\\3",phone))
