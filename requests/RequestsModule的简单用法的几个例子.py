'''
import requests#导入 Requests 模块

r = requests.get('https://github.com/timeline.json')#尝试获取某个网页。本例子中，我们来获取 Github 的公共时间线。
#现在，我们有一个名为 r 的 Response 对象。我们可以从这个对象中获取所有我们想要的信息。

r = requests.post("http://httpbin.org/post")#发送一个 HTTP POST 请求
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
'''

'''
Requests
网络资源（URLs）获取套件。
改善Urllib2的缺点，让使用者以最简单的方式获取网络资源。
可以使用REST操作（POST,PUT,GET,DELETE）存取网络资源。

Requests是用python语言基于urllib编写的，采用的是Apache2 Licensed开源协议的HTTP库，Requests它会比urllib更加方便，可以节约我们大量的工作。

安装：pip install requests


'''
newsurl='https://www.zhihu.com/'
res=requests.get(newsurl)

'''
response.text返回的是Unicode格式，通常需要转换为utf-8格式，否则就是乱码。
response.content是二进制模式，可以下载视频之类的，如果想看的话需要decode成utf-8格式。
不管是通过response.content.decode("utf-8)的方式还是通过response.encoding="utf-8"的方式都可以避免乱码的问题发生。

'''
res.enconding = 'utf-8'
print(res.text)

'''
但是上面获取网页信息的代码出问题了：
<html><body><h1>500 Server Error</h1>
An internal server error occured.
</body></html>

但是把网址换成：
https://www.baidu.com/
之后，得到了网页内容。
网上说这种500错误是对方服务器抗不住压力,所以超时或者发生其它错误，和程序没有太大关系。
'''
