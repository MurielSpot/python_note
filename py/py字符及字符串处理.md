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
b=string.replace(a,'.',' ')#对a进行操作，用空格取代点。
print b
like   the    world
```
