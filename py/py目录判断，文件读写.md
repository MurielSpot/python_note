## 目录操作
### python列出文件夹下所有文件的方法
方法1：使用os.listdir

```
import os
for filename in os.listdir(r'c:\windows'):
    print(filename)#打印出文件夹下文件的名字
```

方法2：使用glob模块，可以设置文件过滤

```
import glob
for filename in glob.glob(r'c:\windows*.exe'):
    print filename
```

方法3：通过os.path.walk递归遍历，可以访问子文件夹

```
import os.path
def processDirectory ( args, dirname, filenames ):
    print 'Directory',dirname
    for filename in filenames:
        print ' File',filename
os.path.walk(r'c:\windows', processDirectory, None )
```

方法4：非递归

```
!/bin/python
import os
for dirpath, dirnames, filenames in os.walk('c:\\winnt'):
    print 'Directory', dirpath
    for filename in filenames:
        print ' File', filename
```

## 判断文件与目录是否存在：

```
import os
os.path.isfile('test.txt') #是否是文件，如果不存在就返回False
os.path.exists(directory) #如果目录不存在就返回False
os.path.isdir(directory) #是否是文件夹
```

## 文件读写
### 文件读写常用函数
- f.write()    #字符串写入文件
- f.writelines   #将一串字符串写入文件。 该序列可以是生成字符串的任何可迭代对象，通常是字符串列表
- f.read([size])   #默认读出文件中所有内容，可以指定size（字节）
- f.readline([size])        #默认每次读取一行，字符串中保留一个尾随的换行字符。
- f.readlines([size])      #默认将文件内容讲到列表中保存
- f.flush()        #将缓冲中的内容写入磁盘
- f.tell()       #显示当前文件的指针所在位置
- f.close()    #关闭打开的文件
- f.seek()       #对文件进行指针偏移操作
