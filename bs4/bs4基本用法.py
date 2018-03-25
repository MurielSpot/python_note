#http://f61be319.wiz03.com/share/s/3S6-cp1BIQ952yXKyj02PIM40CWSe611S4bm27j1H10Isfmp

from bs4 import BeautifulSoup

html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())#格式化输出。
'''
输出：
<html>
 <head>
  <title class="class_title1 class_title2" id="id_title">
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <div>
   <!-- comment test -->
  </div>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
'''

'''
四大对象种类
Tag
通俗点讲就是 HTML 中的一个个标签，像上面的 div，p。每个 Tag 有两个重要的属性 name 和 attrs， 
name 指标签的名字或者 tag 本身的 name，attrs 通常指一个标签的 class。

NavigableString
获取标签内部的文字，如，soup.p.string。

BeautifulSoup
表示一个文档的全部内容。

Comment
Comment对象是一个特殊类型的 NavigableString对象，其输出的内容不包括注释符号
'''
print(type(soup.title))#输出类型。
print(soup.title.name)#姓名。
print(soup.title.attrs)#属性
'''
输出：
<class 'bs4.element.Tag'>
title
{'id': 'id_title', 'class': ['class_title1', 'class_title2']}
'''

print(type(soup.p.string))
print(soup.p.string)#打印p標簽裏的文字.
'''
输出：
<class 'bs4.element.NavigableString'>
The Dormouse's story
'''

print(type(soup))
print(soup.name)
print(soup.attrs)
'''
输出：
<class 'bs4.BeautifulSoup'>
[document]
{}
'''

print(soup.div.string)
print(type(soup.div.string))#注意到上面的div裏是注釋,所以這裏的string是注釋類型的.
print(type(soup.p.string))#p裏不是注釋,所以類型不是注釋類型的.
#另外注意soup.什麽,獲取的是第一個標簽,比如上面獲取的是第一個div,第一個p.
'''
输出：
 comment test 
<class 'bs4.element.Comment'>
<class 'bs4.element.NavigableString'>
'''

'''
遍历文档树

节点内容
.string 属性
获取tag的文本内容 
如果tag只有一个 NavigableString类型子节点,那么这个tag可以使用 .string 得到子节点内容 
如果超过一个, 返回None

多个内容
.strings 属性 获取所有内容, 返回一个generator(包括空白字符) 
.stripped_strings 属性 获取所有内容, 返回一个generator(去除空白字符)

直接子节点
.contents 属性 将tag的子节点以列表的方式输出 
.children 属性 将tag的子节点以list_iterator的方式输出

所有子孙节点
.descendants 属性 对所有子节点递归

父节点
.parent 属性 获取父节点

全部父节点
.parents 属性 获取全部父节点

兄弟节点
.next_sibling 属性 下一个兄弟节点 
.previous_sibling 属性 上一个兄弟节点

全部兄弟节点
.next_siblings 属性 全部的弟弟 
.previous_siblings 属性 全部的哥哥

前后节点
.next_element 属性 后节点 
.previous_element 属性 前节点

所有前后节点
.next_elements 属性 
.previous_elements 属性
'''


