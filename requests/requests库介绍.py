
import requests

url="http://www.baidu.com"

#无参数
r=requests.get(url)
print(r.url)
'''
輸出:
http://www.baidu.com/
'''

#有参数
payload={#設置一個字典類型.
    'key1':'value1',
    'key2':'value2'
}
r=requests.get(url,params=payload)#payload作爲參數傳入.
print(r.url)

#設置header
headers={
    'hello':'world'        
}
r=requests.get(url,headers=headers)
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
####################################################################################3
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





