'''
处理的是一个知乎'发现'的页面.
练习beautifulsoup的使用.
'''

from bs4 import BeautifulSoup

'''
http://www.runoob.com/python/python-func-open.html

py打开文件
python open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。

函数语法
open(name[, mode[, buffering]])
参数说明：
name : 一个包含了你要访问的文件名称的字符串值。
mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
buffering : 如果 buffering 的值被设为 0，就不会有寄存。如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

不同模式打开文件的完全列表：
模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

file 对象方法
file.read([size]) size未指定则返回整个文件,如果文件大小>2倍内存则有问题.f.read()读到文件尾时返回""(空字串)
file.readline() 返回一行
file.readlines([size]) 返回包含size行的列表,size 未指定则返回全部行
for line in f: print line #通过迭代器访问
f.write("hello\n") #如果要写入字符串以外的数据,先将他转换为字符串.
f.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).
f.seek(偏移量,[起始位置]) 用来移动文件指针.
偏移量:单位:比特,可正可负
起始位置:0-文件头,默认值;1-当前位置;2-文件尾
f.close() 关闭文件
'''
f = open(r'C:\Users\oakpa\Desktop\zhihu.html')#用utf-8格式下的编码时,,改用ansii就没问题了.
ftext=f.read()

soup=BeautifulSoup(ftext)

#以标准缩进格式输出
print(soup.prettify())

#取標題soup.title
print(soup.title)
'''
輸出:
<title>发现 - 知乎</title>
'''

#取title裏的字符串
print(soup.title.string)
'''
輸出:
发现 - 知乎
'''

#輸出title標簽的名字,和它的上一級標簽的名字
print(soup.title.name)
print(soup.title.parent.name)
'''
輸出:
title
head
'''

#想先取p的内容,再格式化輸出,發現出錯了.
print(soup.p)
#print(soup.p.pretiffy())#出錯了.
'''
第一句輸出:
<p class="visible-expanded"><a class="answer-date-link meta-item" data-tooltip="s$t$发布于 2018-02-24" href="/question/267647539/answer/327365648" itemprop="url" target="_blank">编辑于 18:24</a></p>
第二句報錯:
TypeError: 'NoneType' object is not callable
'''

#輸出p標簽裏class屬性的内容.
print(soup.p['class'])
'''
輸出:
['visible-expanded']
'''

#輸出a標簽及内容
print(soup.a)#輸出了一條内容
print(soup.find_all('a'))#輸出了多條内容.太長了就不給出輸出内容了.

#輸出id為zh-recommend的内容
print(soup.find(id="zh-recommend"))

#找出所有a標簽中href的内容
for link in soup.find_all('a'):
    print(link.get('href'))
'''
部分輸出:
None
javascript:;
/people/kao-la-bu-hui-fei
#
/question/267647539/answer/327365648
/question/267647539/answer/327365648
javascript:;
#
#
#
#
'''

#从文档中获取所有文字内容:
print(soup.get_text())#獲得文字内容,不過還是有很多空白字符和\u類型的内容.
'''
部分輸出:
© 2018 知乎




{}

<div>
你的帐号由于存在异常?为暂时被限制使?。如需恢复，请
<a target="_blank" href="/account/unblock">解封帐号</a>
</div>

["","","","-1","",0,0]
{"realname_win_config":{"timestamp":1501344000,"tip":"\u5e94\u56fd\u5bb6\u6cd5\u89c4\u5bf9\u4e8e\u5e10\u53f7\u5b9e\u540d\u7684\u8981\u6c42\uff0c\u8fdb\u884c\u4e0b\u4e00\u6b65\u64cd\u4f5c\u524d\uff0c\u9700\u8981\u5148\u5b8c\u6210\u624b\u673a\u7ed1\u5b9a\u3002","continue":0,"continue_time":3600,"skip_ut_verification":0}}
'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''


'''
輸出:

'''
