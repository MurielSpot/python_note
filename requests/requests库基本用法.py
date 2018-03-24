"""
介紹了requests裏get,post的使用方法,還有傳數據和使用cookies時的用法.etc.
"""
import requests

url_get="http://httpbin.org/get"

#无参数
r=requests.get(url_get)
print(r.url)
'''
輸出:
http://httpbin.org/get
'''

#有参数
payload={#設置一個字典類型.
    'key1':'value1',
    'key2':'value2'
}
r=requests.get(url_get,params=payload)#payload作爲參數傳入.
print(r.url)
'''
輸出:
http://httpbin.org/get?key1=value1&key2=value2
'''

#設置header
headers={
    'hello':'world'        
}
r=requests.get(url_get,headers=headers)
print(r.text)
'''
輸出:
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Hello": "world", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "origin": "117.71.156.65", 
  "url": "http://httpbin.org/get"
}
'''
##############################################################################################
url_post="http://httpbin.org/post"#上面是用於get的網址,這裏要改成post,因爲要測試post.

#基本post請求
#有數據
payload={
    'hello':'world'
}
r=requests.post(url_post,data=payload)
print(r.text)
'''
輸出:
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "hello": "world"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "117.71.156.65", 
  "url": "http://httpbin.org/post"
}
'''

#有數據(json格式)
import json#自帶的
payload={
    'hello':'world'
}
r=requests.post(url_post,data=json.dumps(payload))#把傳入的數據格式改成json格式的.
print(r.text)
"""
輸出:注意這裏和普通有數據post的區別,form沒有數據,data有數據了,json裏也能看到helloworld.
{
  "args": {}, 
  "data": "{\"hello\": \"world\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "18", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": {
    "hello": "world"
  }, 
  "origin": "117.71.156.65", 
  "url": "http://httpbin.org/post"
}
"""

##############################################################################################
#上傳文件
files={
     'file':open(r'C:\Users\oakpa\Desktop\test.txt','rb')#rb二進制可讀.
}
r=requests.post(url_post,files=files)
print(r.text)
"""
輸出:
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "<body>\r\nbody here\r\n\t<div class=\"c\">class=\"c\"</div>\r\n\t<div id=\"i\">id=\"i\"</div>\r\n\t<div>div</div>\r\n</body>"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "247", 
    "Content-Type": "multipart/form-data; boundary=48f999d4c94047cb8f037ffcae0b4a5f", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "117.71.156.65", 
  "url": "http://httpbin.org/post"
}
"""

##############################################################################################
url_coo="http://httpbin.org/cookies"

#使用cookies
coo=dict(cookies_are='working')#用dict返回的就是一個字典,和用大括號寫效果是一樣的.

r=requests.get(url_coo,cookies=coo)
print(r.text)
"""
輸出:
{
  "cookies": {
    "cookies_are": "working"
  }
}
"""

##############################################################################################
url_github="http://github.com"

#請求超時配置.
r=requests.get(url_github,timeout=0.001)
print(r.text)
"""
輸出:
ConnectTimeout: HTTPConnectionPool(host='github.com', port=80): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x00000255EA418F98>, 'Connection to github.com timed out. (connect timeout=0.001)'))
"""

##############################################################################################
url_connection="http://httpbin.org/cookies/set/sessioncookie/123456789"

#持久會話
#沒有持久會話的情況
requests.get(url_connection)#第一次get
r=requests.get("http://httpbin.org/cookies")#第二次獲取不到cookies.
print(r.text)
"""
輸出:
{
  "cookies": {}
}
"""
#設置持久會話的情況
s=requests.session()
s.get(url_connection)#用s訪問.
r=s.get("http://httpbin.org/cookies")#再次get獲取cookies.
print(r.text)
"""
輸出:
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
"""

##############################################################################################
#使用代理(可以防止ip被封)
proxies={
    'http':'http://41.118.132.69:4433'#這是一個廢掉的ip,用它來測試.
}
r=requests.get("http://www.baidu.com",proxies=proxies)
print(r.status_code)
"""
輸出:
ProxyError: HTTPConnectionPool(host='41.118.132.69', port=4433): Max retries exceeded with url: http://www.baidu.com/ (Caused by ProxyError('Cannot connect to proxy.', NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000255EA0B0B38>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。',)))
"""

r=requests.get("http://www.baidu.com")#再用自己的ip訪問.
print(r.status_code)
"""
輸出:
200
"""

##############################################################################################
