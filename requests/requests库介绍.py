
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
