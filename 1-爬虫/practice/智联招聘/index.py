import requests,re,json

def getMsg(page=1):
    url=f"https://fe-api.zhaopin.com/c/i/sou?start={90*page}&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3&=0&at=f85ecb422b4345bfad4a74490befe832&rt=43d725f9157e4d9b891e2360d26cb6ad&_v=0.09973825&userCode=694164501&x-zp-page-request-id=15bc43788fb24e108c917b69050771c6-1568967144474-833293&x-zp-client-id=57ae38da-1c58-469c-9ec4-fa4c7ded0877"
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "referer":"https://www.zhaopin.com/shanghai/",
        "cookie":"urlfrom=121113803; urlfrom2=121113803; adfbid=0; adfbid2=0; x-zp-client-id=57ae38da-1c58-469c-9ec4-fa4c7ded0877; sts_deviceid=16d4dac1599b16-017eb34146fe18-5373e62-2073600-16d4dac159a32e; sts_sg=1; sts_sid=16d4dac159c33d-07c4e91424d8da-5373e62-2073600-16d4dac159dc15; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAs0M9CwI00000P_OfNC0000052bheg.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15yf1nA79mvcYnj0snAfzuj00IHYkP1m1wb77njRdrHF7fWKDPDujPjT3wD7DPYN7fHTkwfK95gTqFhdWpyfqn1c3rjb4rjc4PiusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Y1n1fkns%26tpl%3Dtpl_11534_19968_16032%26l%3D1514225627%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3288998295_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D64%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26oq%3Dqq%2525E9%25259F%2525B3%2525E4%2525B9%252590%26inputT%3D4162%26prefixsug%3D%2525E6%252599%2525BA%2525E8%252581%252594%26rsp%3D0; sajssdk_2015_cross_new_user=1; at=f85ecb422b4345bfad4a74490befe832; rt=43d725f9157e4d9b891e2360d26cb6ad; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22694164501%22%2C%22%24device_id%22%3A%2216d4dac15aa997-047705259ab858-5373e62-2073600-16d4dac15ab924%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAs0M9CwI00000P_OfNC0000052bheg.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15yf1nA79mvcYnj0snAfzuj00IHYkP1m1wb77njRdrHF7fWKDPDujPjT%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2216d4dac15aa997-047705259ab858-5373e62-2073600-16d4dac15ab924%22%7D; dywea=95841923.1465726869047435800.1568966224.1568966224.1568966224.1; dywec=95841923; dywez=95841923.1568966224.1.1.dywecsr=landing.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/register; ZP_OLD_FLAG=false; jobRiskWarning=true; __utma=269921210.2112303682.1568966224.1568966224.1568966224.1; __utmc=269921210; __utmz=269921210.1568966224.1.1.utmcsr=landing.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/register; __utmt=1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568966224; privacyUpdateVersion=2; acw_tc=2760820e15689662376466376e2829f34c647814a98850a9fa20e0b96875f1; sou_experiment=psapi; POSSPORTLOGIN=5; CANCELALL=1; dyweb=95841923.2.10.1568966224; __utmb=269921210.2.10.1568966224; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568966403; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22da359ae1-a032-4086-8fa2-eb0ec0c74430-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//www%22:{%22seid%22:%22f85ecb422b4345bfad4a74490befe832%22%2C%22actionid%22:%22278f2914-0a7a-4e54-9356-4b74e467a3d9-cityPage%22}}; sts_evtseq=18"
    }

    html=requests.get(url,headers=headers)
    dict=json.loads(html.text)
    jobList=dict['data']['results']
    Msgs=[]
    for job in jobList:
        name=job['jobName']
        companyName=job['company']['name']
        salary=job['salary']
        edulevel=job['eduLevel']['name']
        Msgs.append({
            "name":name,
            "companyName":companyName,
            "salary":salary,
            "edulevel":edulevel
        })
    return Msgs
def save_Msg(Msgs):
    with open("./智联招聘.csv",'a',encoding="utf-8")as file:
        for msg in Msgs:
            file.write("%s,%s,%s,%s\n"%(msg['name'],msg['companyName'],msg['salary'],msg['edulevel']))


for i in range(1,13):
    save_Msg(getMsg(i))
    print(f"第{i}页数据保存完成")


