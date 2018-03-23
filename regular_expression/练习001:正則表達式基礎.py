
# -*- coding: utf-8 -*-

'''
正則表達式:是用來記錄文本規則的代碼.

11位數字.
以1開頭.

\ 將下一個字符標記為特殊字符.
如:\d 代表0到9中的一個數字.

定界符:
^ 匹配輸入字符串開始的位置.
$ 匹配輸入字符串結束的位置.
\b 匹配一個單詞邊界,也就是指單詞和空格閒的位置.
\B 匹配非單詞邊界.


個數/次數
* 匹配前面的子表達式0次或多次.
+ 匹配前面的子表達式1次或多次.
? 匹配前面的子表達式0次或1次.
{n} n是一個非負整數.
{n,} n是一個非負整數.
{n,m} m和n均爲非負整數,其中n<=m.

? 儅該字符緊跟在任何一個其它限制符(*,+,?,{n},{n,},{n,m})後面時,匹配模式是非貪婪的.
. 匹配除'\n'之外的任何單個字符.

x|y 匹配除'\n'之外的任何單個字符.

[xyz] 字符集合
[^xyz] 負值字符集合.
[a-z] 字符範圍
[^a-z] 負值字符範圍.

空白符:
\f 匹配一個換頁符.
\n 匹配一個換行符.
\r 匹配一個回車符.
\t 匹配一個製表符.

語法糖:
\d 匹配一個數字字符.[0-9]
\D 匹配一個非數字字符.[^0-9]
\s 匹配任何空白字符,包括空格,制表符,換頁符等.等同於[\f\n\t\r\v].
\S 匹配任何非空白字符.等同於[^\f\n\t\r\v].
\w 匹配字母,數字,下劃綫.等同於[A-Za-z0-9].
\W 匹配非字母,數字,下劃綫.等同於[^A-Za-z0-9].

在python中使用正則表達式,需要一個re模塊.這個模塊python中自帶,不需要暗轉,但需要引入.
常用的函數有:
查找:
    re.search
    re.findall
替換:
    re.sub
'''

import re

test='hello'
result1=re.search('l',test)#匹配了第一個,後面的沒有管.
print(result1)
result2=re.findall('l',test)#返回列表,含有所有匹配的結果.
print(result2)
result3=re.sub('l','yo',test)#將test裏的l都換成yo.
print(result3)
