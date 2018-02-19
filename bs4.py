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
