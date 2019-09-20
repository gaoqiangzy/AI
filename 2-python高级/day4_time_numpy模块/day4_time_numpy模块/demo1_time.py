import time

# 生成时间戳  time.time()
print(time.time())

# 转换成日期格式
time.ctime() 接收时间戳,返回时间字符串
print(time.ctime(1888888888)) #Fri Nov  9 11:21:28 2029

# ctime() 转换出来的对国人来说不友好,想要转换成 2019-08-30 09:44:56
time.strftime() 把时间元组转换为时间字符串
time_tuple=time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuple))

# 把日期字符串转换成时间元组-时间戳
# time.strptime(时间字符串,格式化)
time_str=input("请输入时间(2010-10-20 12:30:30)")
print(time.mktime(time.strptime(time_str,"%Y-%m-%d %H:%M:%S")))


# 转换成时间元组
# time.gmtime(time_stamp)  # 不传参数的时候,默认为当前时间
# time.localtime(time_stamp)  *
print(time.gmtime())
print(time.localtime(1000000000))


time.process_time()
s=time.process_time()
#
for i in range(100000000):
    pass
#
print(time.process_time()-s)


time_str="2019-09-01 12:00:00"
time_stamp=time.mktime(time.strptime(time_str,"%Y-%m-%d %H:%M:%S"))
time_stamp-=(3*24*60*60)
print(time.localtime(time_stamp))
print(time.process_time())
