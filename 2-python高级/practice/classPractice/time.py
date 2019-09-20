import time
# 返回格林威治西部的夏令时地区的偏移秒数
print(time.altzone)

# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# print(time.asctime())

# 在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后包括第三个的调用是自第一次调用以后到现在的运行时间。
# print(time.process_time())

# 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print(time.ctime())
print(type(time.ctime()))

# 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t
print(time.gmtime())
print(type(time.gmtime()))

# 接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t
print(time.localtime())
print(type(time.localtime()))

# 接受时间元组并返回时间辍
print(time.mktime(time.localtime()))

# 推迟调用线程的运行，secs指秒数。
time.sleep(2)

# 接收以时间元组，并返回指定格式可读字符串表示的当地时间，格式由fmt决定。
print(time.strftime("yy-mm-dd hh-mm-ss",time.localtime()))

# 根据fmt的格式把一个时间字符串解析为时间元组,str需要和fmt一一对应,
# 如strptime(‘20 3’,“%d %m”)%d表示一个月第几天,%m表示一年的第几个月
print(time.strptime("2017-10-10 23:40:00","%d %m"))

# 返回当前时间的时间戳
print(time.time())
