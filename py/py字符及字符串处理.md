## 字符串操作常用函数

split函数：这里的示例应该是py2.x
```
print b
like   the    world
list1=b.split()#把空格过滤出去，剩下的组成一个list，也可以在split()的括号里传入一个参数
print list1
['like', 'the', 'world']
```

join函数：这里的示例应该是py2.x
```
list1
['like', 'the', 'world']
delimiter=' '
line=delimiter.join(list1)
print line
like the world
```

## 如何去掉空白字符
string.strip(s)，s是一个序列，在string的两边删除string中在序列s中的字符。
- string.lstrip(s)   在string的左边删除string中在序列s中的字符。
- string.rstrip(s)   在string的右边删除string中在序列s中的字符。
- 若没有s，则删除空白符（包括'\n', '\r',  '\t',  ' ')。

import re
- re.sub('\s','',string)  将string中的所有空白字符删除
- re.sub(['\"','\'','\s'],'',string)  将string中的所有空白字符及单双引号删除。

## 替换字符串中的内容string.replace()
首先需要：import string<br/>
然后有两种方法取代字符串中的某项：

方法1：
```
a='...like...the....world............'
b=a.replace('.',' ')#用空格取代点。
print b
like   the    world
```

方法2：
```
a='...like...the....world............'
b=string.replace(a,'.',' ')#对a进行

## 读取utf-8格式的txt文件，开头出现不明字符\xef\xbb\xbf
读取的时候第一个元素为‘\xef\xbb\xbf1883’，上网看了一些资料，原来在python的file对象的readline以及readlines程序中，针对一些UTF-8编码的文件，开头会加入BOM来表明编码方式。 <br/>
解决方法有很多种： 

- [这篇博客引用](http://www.cnblogs.com/nx520zj/p/5869241.html)codecs模块，来判断前三个字节是否为BOM_UTF8。如果是，则剔除\xef\xbb\xbf字节。 
- 另外还有很多解决方案，可以判断列表中是否有\xef\xbb\xbf字符，如果有，用replace()替换为空的，代码如下：<br/>
  if '\xef\xbb\xbf'  in line:<br/>
  	str1 = line.replace('\xef\xbb\xbf','')#用replace替换掉'\xef\xbb\xbf'<br/>
