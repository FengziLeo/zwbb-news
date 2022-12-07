import json
import requests
import time

def log(ip):
    #url = "http://whois.pconline.com.cn/ipJson.jsp?ip={}&json=true".format(ip)
    url = 'https://api.ip138.com/ip/?ip={}&datatype=jsonp&token=4ed484c90dacb0ff55e6fde8d0bd34ab'.format(ip)
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
