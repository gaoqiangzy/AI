import requests,re

url="https://search.51job.com/list/030200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Referer":"https://www.51job.com/"
}
r=requests.get(url,headers=headers)
html=r.content.decode('gbk')
# <a target="_blank" title="PHP软件测试工程师/初级" href="https://jobs.51job.com/guangzhou-thq/108918914.html?s=01&t=0"  onmousedown="">
#                     PHP软件测试工程师/初级                </a>
# <a target="_blank" title="嵌入式软件测试工程师" href="https://jobs.51job.com/guangzhou-thq/116461929.html?s=01&t=0"  onmousedown="">
#                     嵌入式软件测试工程师                </a>
# <a target="_blank" title="软件测试工程师" href="https://jobs.51job.com/shenzhen-ftq/116482190.html?s=01&t=0"  onmousedown="">
#                     软件测试工程师                </a>

# 得到职位名和url
# job_info_regex='<a target="_blank" title="(.*?)" href="(.*?)"  onmousedown="">\s\s.*?</a>'
# job_name_url=re.findall(job_info_regex,html)
# 得到公司名
# company=re.findall('<span class="t2"><a target="_blank" title=".*?" href=".*?">(.*?)</a></span>',html)
# print(company)
# 得到职位地址
# position=re.findall('<span class="t3">(.*?)</span>',html)
# print(position)

# 得到薪资
# salary=re.findall('<span class="t4">(.*?)</span>',html)
# print(salary)

# 发布时间
# addtime=re.findall('<span class="t5">(.*?)</span>',html)
# print(addtime)

# 合并多个列表
# infos=list(map(lambda w,x,y,z,a:{'name':w[0],'url':w[1],"company":a,'position':x,"salary":y,'addtime':z},job_name_url,position[1:],salary[1:],addtime[1:],company))
# for once in infos:
#     print(once)

# 一次性的取出 某一个系列,然后再把多个值合并到一个,可能会出现的一个问题是,如果有的信息没有,就会导致,多个序列的长度不同,然后拼接的时候,就会有问题
# 我们先把每一个大的条目取出来


all_div=re.findall('<div class="el">(.*?)</div>',html,re.DOTALL) # re.DOTALL 模式,是点可以匹配所有,包括换行
for once_div in all_div:
    job_info_regex = '<a target="_blank" title="(.*?)" href="(.*?)"  onmousedown="">\s\s.*?</a>'
    job_name=re.search(job_info_regex,once_div).group(1)
    job_url=re.search(job_info_regex,once_div).group(2)
    company=re.search('<span class="t2"><a target="_blank" title=".*?" href=".*?">(.*?)</a></span>',once_div).group(1)
    position = re.search('<span class="t3">(.*?)</span>', once_div).group(1)
    salary = re.search('<span class="t4">(.*?)</span>', once_div).group(1)
    addtime = re.search('<span class="t5">(.*?)</span>', once_div).group(1)
    print({"job_name":job_name,"job_url":job_url,"company":company,"position":position,"salary":salary,"addtime":addtime})
