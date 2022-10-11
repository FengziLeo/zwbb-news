# -*- coding: utf-8 -*-

import uvicorn
from spider import Spider
from weibospider import spider_weibo
from fastapi import FastAPI
from threading import Timer
from threading import Thread
import time


data_zhihu = []     #知乎
data_tieba = []     #贴吧
data_baidu = []     #百度
data_bsite = []     #B站
data_weibo = []     #微博
zwb_time_data = {}
b_time_data = {}

s = Spider()

def run_tieba():
    global data_tieba
    data_tieba = s.spider_tieba()

def run_zhihu():
    global data_zhihu
    data_zhihu = s.spider_zhihu()
    
def run_weibo():
    global data_weibo
    data_weibo = spider_weibo()

def run_bsite():
    global data_bsite
    data_bsite = s.spider_bsite()

def run_baidu():
    global data_baidu
    data_baidu = s.spider_baidu()

def zwb_time():
    global zwb_time_data
    zwb_time_data["time"]=(str(time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))))

def b_time():
    global b_time_data
    b_time_data["time"]=(str(time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))))


#此组15分钟采集一次
def task1():
    #多线程运行
    Thread(target=run_zhihu,).start()
    Thread(target=run_tieba,).start()
    Thread(target=run_weibo,).start()
    Thread(target=run_baidu,).start()
    Thread(target=zwb_time,).start()
    Timer(15*60,task1,).start()

#此组每天采集一次
def task2():
    #多线程运行
    Thread(target=run_bsite,).start()
    Thread(target=b_time,).start()
    Timer(24*60*60,task2,).start()

task1()
task2()

app = FastAPI()
@app.get("/")
def index():
    return {'hello':'world!'}

@app.get("/hot/{name}")
def read_name(name: str):
    if name == 'zhihu':
        return data_zhihu
    elif name == 'weibo':
        return data_weibo
    elif name == 'tieba':
        return data_tieba
    elif name == 'bsite':
        return data_bsite
    elif name =='baidu':
        return data_baidu
    client_host_ip = request.client.host
    print(client_host_ip)

@app.get("/time/{name}")
def zwb(name: str):
    if name == 'zwb':
        return zwb_time_data
    elif name == 'b':
        return b_time_data


if __name__ == '__main__':
    uvicorn.run(app=app,
                host="127.0.0.1",
                port=80)

    

