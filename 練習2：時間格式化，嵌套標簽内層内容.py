'''
抓取新浪網新聞時間，並對時間進行格式化處理。
獲取多層標簽嵌套時，内層的内容。
'''
import requests
from bs4 import BeautifulSoup

from datetime import datetime

url='http://finance.sina.com.cn/chanjing/gsnews/2018-02-22/doc-ifyrswmu9224499.shtml'

res=requests.get(url)
res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')

xldate=soup.select('.date')#找class為date的部分，提取時間。
time=[]
for d in xldate:
    time.append(d.text)

#用datetime把日期轉化為規則的格式。
time2=[]
for t in time:
    time2.append(datetime.strptime(t,'%Y年%m月%d日 %H:%M'))
print(time2)#可以看到年月日時間已經被存起來了。
print(time2[0].strftime('%Y-%m-%d %H:%M'))#轉換囘字串的格式。

#先選了class屬性為top-bar的標簽，然後在裏面選擇div標簽。
tb=soup.select('.top-bar-inner div')[0]
print(tb)

'''
網頁源碼：
<div class="top-bar-inner clearfix">
<div class="second-title">万达确将重返中国足坛 今年难办股权转让或只能冠名</div>
</div>

結果：
<div class="second-title">万达确将重返中国足坛 今年难办股权转让或只能冠名</div>
'''
