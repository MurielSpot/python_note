'''
1. 下载
2. 解压zip
'''

# 1-------------------------------------------
# 文件下载工具
import urllib.request
url="https://github.com/dav/word2vec/archive/master.zip"
filepath="word2vec.zip"
result=urllib.request.urlretrieve(url,filepath)

# 2-------------------------------------------
# 解压zip工具
import zipfile
file="./word2vec.zip"
extractPath="code"
z = zipfile.ZipFile(filepath, 'r')
z.extractall(extractPath)

# -------------------------------------------

# -------------------------------------------

# -------------------------------------------

# -------------------------------------------

# -------------------------------------------

# -------------------------------------------

# -------------------------------------------
