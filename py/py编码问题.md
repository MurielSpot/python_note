##### 编码的转换
以下说法基于python2.x：<br/>
str(s)和unicode(s)分别返回str字符串对象和Unicode字符串对象。
<br/>str(s)是s.encode('ascii')的简写，即执行str(s)相当于执行s.encode('ascii')，所以如果用str(s)输出s字符串里的中文，会报错，应该指定正确的编码，再str，比如str(s.encode('gbk'))是将数据按gbk格式解释，再把它转为字符串对象。
<br/>unicode有同样的问题，unicode(ss)等效于ss.decode('ascii'),因此要正确转换就要指定编码，如ss.decode('gbk')。
<br/>为防止乱码问题，最好始终使用同一种编码格式进行编码和解码操作。

##### python中的encode和decode
参考：https://www.cnblogs.com/vipchenwei/p/6993788.html<br/>
decode的作用是将其他编码的字符转换成unicode编码,如str1,decode('gb2312'),表示将gb2312编码的字符串str1转换成unicode编码。<br/>
encode的作用是将unicode编码转换成其他编码的字符串,如str2,encode('gb2312'),表示将unicode编码的字符串str2转换成gb2312编码。<br/>


##### python的默认编码

如果不在python文件指定头信息＃-*-coding:utf-8-*-,那就使用默认的python2中默认使用ascii，python3中默认使用utf-8。<br/>


##### 内存与硬盘中的编码

读取已经加载到内存的代码（unicode编码的二进制），然后执行，执行过程中可能会开辟新的内存空间，比如x="hello"。<br/>
**内存的编码使用unicode，不代表内存中全都是unicode编码的二进制**，在程序执行之前，内存中确实都是unicode编码的二进制,比如从文件中读取了一行x="hello",其中的x，等号，引号，地位都一样，都是普通字符而已，都是以unicode编码的二进制形式存放与内存中的.但是程序在执行过程中，会申请内存（与程序代码所存在的内存是俩个空间），可以存放任意编码格式的数据，比如x="hello",会被python解释器识别为字符串，会申请内存空间来存放"hello"，然后让x指向该内存地址，此时新申请的该内存地址保存也是unicode编码的hello,如果代码换成x="hello".encode('utf-8'),那么新申请的内存空间里存放的就是utf-8编码的字符串hello了.
