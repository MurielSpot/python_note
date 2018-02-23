import requests
from bs4 import BeautifulSoup

url='http://finance.sina.com.cn/chanjing/gsnews/2018-02-22/doc-ifyrswmu9224499.shtml'

res=requests.get(url)
res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')

article=[]
for i in soup.select('.article p')[1:-1]:#[1:-1]表示把第一個p和最后一個p去掉。
    article.append(i.text.strip())#strip用來把空白字符去掉。

t='<html>\
<body>\
<p>some some thing some</p>\
</body>\
<html>'
s=BeautifulSoup(t,'html.parser')
print(s.text.strip('some'))#將s文字裏兩頭的some去掉了。
print(s.text.lstrip('some'))#將s中的文字，從左邊去掉了some。
'''
要處理的文字：some some thing some
結果：
 some thing 
 some thing some
'''
    
print('-------------'.join(article))#join更具前面引號的内容，對list裏的内容進行合并。這裏是根據空白進行合并，得到一個新字串。
print(article)#但打印原list還是列表，不帶分隔符。

'''
Python中有join()和os.path.join()两个函数，具体作用如下：
    join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    os.path.join()：  将多个路径组合后返回

一、函数说明
1、join()函数

语法：  'sep'.join(seq)

参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串

返回值：返回一个以分隔符sep连接各个元素后生成的字符串

 

2、os.path.join()函数

语法：  os.path.join(path1[,path2[,......]])

返回值：将多个路径组合后返回

注：第一个绝对路径之前的参数将被忽略
'''
