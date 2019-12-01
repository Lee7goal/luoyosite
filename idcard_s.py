import requests
from lxml import etree


def SearchId(userid):
    link = 'http://qq.ip138.com/idsearch/index.asp'
    data = {
        'userid': userid,
        'action': 'idcard'
    }

    res = requests.get(link, data)
    res.encoding = 'utf-8'
    need_str = res.text

    html = etree.HTML(need_str)
    hrefs = html.xpath('//p')
    tmp_list = []
    for href in hrefs:
        tmp_list.append(href.text)
    return tmp_list
