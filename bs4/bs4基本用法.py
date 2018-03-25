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
