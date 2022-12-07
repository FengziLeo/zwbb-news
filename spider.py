# -*- coding: utf-8 -*-

import json
import requests
from lxml import etree
from threading import Timer

from ciyun import CY

baidu_api = "https://top.baidu.com/api/board?platform=wise&tab=realtime"
bsite_api = 'https://www.bilibili.com/v/popular/rank/all'
weibo_api = "https://s.weibo.com/top/summary/"
tieba_api = "http://tieba.baidu.com/hottopic/browse/topicList?res_type=1"
zhihu_api = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

#组装数据
def packdata(para_data):
    list_data = []
    for i in para_data:
        data = {}
        data["title"]=i[0]
        data["url"]=i[1]
        list_data.append(data)
    return list_data
    #return data
    
class Spider(object):
    def __init__(self,url=None):
        if url!=None:
            self.ur0l = url
            self.res = requests.get(url,headers=headers)
            self.res.encoding = "utf-8"
            self.soup = etree.HTML(self.res.text)


    #知乎热榜
    def spider_zhihu(self):
        list_zhihu = [] #此列表用于储存解析结果
        res = Spider(zhihu_api).res  
        #逐步解析接口返回的json
        zhihu_data = json.loads(res.text)['data']
        for part_zhihu_data in zhihu_data:              #遍历每一个data对象
            zhihu_id = part_zhihu_data['target']['id']    #从对象得到问题的id
            zhihu_title = part_zhihu_data['target']['title'] #从对象得到问题的title
            list_zhihu.append([zhihu_title,zhihu_id])
        return packdata(list_zhihu)
    
    #微博热搜见weibospider

    #贴吧热度榜单
    def spider_tieba(self):
        list_tieba = []
        soup = Spider(tieba_api).soup
        for soup_a in soup.xpath("//a[@class='topic-text']"):
            tieba_title = soup_a.text
            tieba_url = soup_a.get('href')
            list_tieba.append([tieba_title,tieba_url])
        return packdata(list_tieba)


    #B站排行榜
    def spider_bsite(self):
        list_bsite = []
        soup = Spider(bsite_api).soup
        for i in soup.xpath("//div[@class='info']/a"):
            bsite_title = i.xpath('text()')[0]
            bsite_url = i.get('href')
            list_bsite.append([bsite_title,bsite_url])
        return packdata(list_bsite)

    #百度
    def spider_baidu(self):
        ciyun = ''
        list_baidu = []
        titles = []
        url = []
        res = Spider(baidu_api).res
        json_data = res.json()
        jsondata = json_data['data']['cards'][0]['content']
        for data in jsondata:
            new_url = str(data['url'])
            new_url = new_url[0:8] + new_url[10::]
            titles.append(data['word'])
            url.append(new_url)
        for i in range(30):
            list_baidu.append([titles[i],url[i]])
            ciyun = ciyun + titles[i]
        CY(ciyun,'baidu')
        return packdata(list_baidu)

        

