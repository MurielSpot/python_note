from bs4 import BeautifulSoup #anaconda内建有beautifulsoup

html_sample='\
<html>\
<body>\
<h1 id="title">Hello world</h1>\
<a href="#" class="link">this is the link</a>\
<a href="# link2" class="link">this is link2</a>\
</body>\
<html>'

soup=BeautifulSoup(html_sample,'html.parser') #如果不明确使用什么parser（剖析器），会给出警告它自己选用了一个比较好的剖析器，但是不能保证在任何环境下都能有好的结果。
print(type(soup))
print(soup.text)

'''
结果：
<class 'bs4.BeautifulSoup'>
Hello worldthis is the linkthis is link2
'''

#使用select，找出含有一些標簽的元素。回傳的是一個list。
soup=BeautifulSoup(html_sample,'html.parser')
header=soup.select('h1')
print(header)
print(header[0]) #取出list其中的一個。
print(header[0].text) #把文字取出來。

alink=soup.select('a')
print(alink)
for link in alink:
    print(link.text) #依次打出alink裏的内容。


