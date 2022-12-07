import json
import requests
import time

def log(ip):
    #url = "http://whois.pconline.com.cn/ipJson.jsp?ip={}&json=true".format(ip) 
    url = 'https://api.ip138.com/ip/?ip={}&datatype=jsonp&token=**'.format(ip) #这里我使用的是ip138的接口，感觉较准，但是是收费的，也可以用上一行免费的接口，需要将代码简单修改即可
    req = requests.get(url).text
    json1 = json.loads(req)
    #ip_addr = json1["addr"]
    ip_addr = json1["data"]
    ipaddr = ''
    for i in range(5):
        ipaddr = str(ip_addr[i]) + ipaddr
    fileName='log/{}.log'.format(time.strftime("%Y.%m.%d"))
    nowtime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with open(fileName,'a',encoding='utf-8')as file:
        file.write(nowtime +'   ' + ip + '   ' + ipaddr + '\n')

log('8.141.153.100')
