## 如何去掉空白字符

string.strip(s)，s是一个序列，在string的两边删除string中在序列s中的字符。
- string.lstrip(s)   在string的左边删除string中在序列s中的字符。
- string.rstrip(s)   在string的右边删除string中在序列s中的字符。
- 若没有s，则删除空白符（包括'\n', '\r',  '\t',  ' ')。

import re
- re.sub('\s','',string)  将string中的所有空白字符删除
- re.sub(['\"','\'','\s'],'',string)  将string中的所有空白字符及单双引号删除。
