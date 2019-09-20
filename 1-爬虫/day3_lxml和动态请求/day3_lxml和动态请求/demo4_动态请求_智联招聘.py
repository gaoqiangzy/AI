import requests,json
from lxml import etree

url="https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=php&kt=3&=0&_v=0.06845485&x-zp-page-request-id=a02d19a448254ff194ef0e86802753c8-1567232161700-511123&x-zp-client-id=530d7f62-64db-4a94-8173-37dd8084f88b"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer":"https://sou.zhaopin.com/?p=2&jl=538&sf=0&st=0&kw=php&kt=3"
}
r=requests.get(url,headers=headers)
# print(r.text)
# print(type(r.text))
resp_dict=json.loads(r.text)

# print(resp_dict)
joblist=resp_dict['data']['results']
joblist.sort(key=lambda x:x['vipLevel'])
for once in joblist:
    name=once['jobName']
    salary=once['salary']
    edulevel=once['eduLevel']['name']
    workexp=once['workingExp']['name']
    print(name,salary,edulevel,workexp)