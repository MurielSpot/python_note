'''
Requests
网络资源（URLs）获取套件。
改善Urllib2的缺点，让使用者以最简单的方式获取网络资源。
可以使用REST操作（POST,PUT,GET,DELETE）存取网络资源。

'''
newsurl='https://www.zhihu.com/'
res=requests.get(newsurl)
print(res.text)

