from lxml import etree
import requests




BASE_URL = 'https://s.weibo.com'


def getHTML(url):
    ''' 获取网页 HTML 返回字符串

    Args:
        url: str, 网页网址
    Returns:
        HTML 字符串
    '''
    # Cookie 有效期至2023-02-10
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': 'SUB=_2AkMVWDYUf8NxqwJRmP0Sz2_hZYt2zw_EieKjBMfPJRMxHRl-yj9jqkBStRB6PtgY-38i0AF7nDAv8HdY1ZwT3Rv8B5e5; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFencmWZyNhNlrzI6f0SiqP'
    }
    response = requests.get(url, headers=headers)
    if response.encoding == 'ISO-8859-1':
        response.encoding = response.apparent_encoding if response.apparent_encoding != 'ISO-8859-1' else 'utf-8'
    return response.text


# 使用 xpath 解析 HTML
def parseHTMLByXPath(content):
    ''' 使用 xpath 解析 HTML, 提取榜单信息

    Args:
        content: str, 待解析的 HTML 字符串
    Returns:
        榜单信息的字典 字典
    '''
    html = etree.HTML(content)

    titles = html.xpath(
        "//tr[position()>1]/td[@class='td-02']/a[not(contains(@href, 'javascript:void(0);'))]/text()")
    hrefs = html.xpath(
        "//tr[position()>1]/td[@class='td-02']/a[not(contains(@href, 'javascript:void(0);'))]/@href")
    
    titles = [title.strip() for title in titles]

    hrefs = [BASE_URL + href.strip() for href in hrefs]


    weibo_data=[]
    for i in range(50):
        weibo_data.append([titles[i],hrefs[i]])

    list_data = []
    for n in weibo_data:
        data = {}
        data["title"]=n[0]
        data["url"]=n[1]
        list_data.append(data)
    return list_data




def spider_weibo():
    url = '/top/summary'
    content = getHTML(BASE_URL + url)
    correntRank = parseHTMLByXPath(content)
    return correntRank
