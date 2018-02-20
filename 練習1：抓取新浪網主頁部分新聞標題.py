import requests

from bs4 import BeautifulSoup

xlurl='http://www.sina.com.cn/'

res=requests.get(xlurl)
res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')
for link in soup.select('.news_top'): #a標簽裏的class有一個值為news_top，找出class為news_top的部分，下一行打印出了其中的内容。
    print(link.text)

'''
結果：
习近平和他的父母 牵妈妈的手
你养我长大 我陪你变老 新春走基层
微视频《新时代 向心力》 理上网来 暖新闻
傅莹驳“中国威胁论” 马蒂斯忙为美对华政策辩护
英国开发商发话：让印度拿下这个酷炫的世界第一
又有企业家网络上表达利益诉求 实名举报市委书记懒政
《年味》第三季：在衣食住行中品年的味道
这10个小常识拯救上亿中国人生命 最后一个太重要

'''
