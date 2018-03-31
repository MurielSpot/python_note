
'''
http://f61be319.wiz03.com/share/s/3S6-cp1BIQ952yXKyj02PIM40CWSe611S4bm27j1H10Isfmp
###########################################################################################
遍历文档树

节点内容
.string 属性
获取tag的文本内容 
如果tag只有一个 NavigableString类型子节点,那么这个tag可以使用 .string 得到子节点内容 
如果超过一个, 返回None

多个内容
.strings 属性 获取所有内容, 返回一个generator(包括空白字符) 
.stripped_strings 属性 获取所有内容, 返回一个generator(去除首尾的空白字符)

    from bs4 import BeautifulSoup
    test="""
    <html>
    <body>
    <p>a_p</p>
    <p>b_p</p>
    <div>abc<br/>      ab   c</div>
    </body>
    </html>
    """
    soup=BeautifulSoup(test,'lxml')
    print(soup.p.string)#输出a_p,第二个p被忽略了。
    print(soup.div.string)#输出None，因为div里有大于一个NavigableString类型子节点，所以输出None。
    print(soup.div.strings)#<generator object _all_strings at 0x000002B15F0D43B8>
    print(list(soup.div.strings))#['abc', '      ab   c']
    print(soup.div.stripped_strings)#<generator object stripped_strings at 0x000002B15F0D4888>
    print(list(soup.div.stripped_strings))#['abc', 'ab   c']

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

###########################################################################################
搜索文档树

find_all() 当前标签的所有子节点，返回一个列表。
1. 通过标签名查找
如：soup.find_all('p')就是在整个soup里查找p。
soup.div.find_all('p')是在div里找。
2. 通过正则查找
如：soup.find_all(re.compile('^p'))查找p开头的标签。
3. 通过列表查找
如：print(soup.find_all(['p', 'div']))中p和div标签都可以找到。
4. 通过正则配合内容查找，返回的是列表，列表里是内容。
如：print(soup.find_all(text=re.compile('content$')))找以content结尾的内容，组成一个列表。
    from bs4 import BeautifulSoup
    import re
    html="""
    <html><head></head>
    <body>
    <p><b>p-content1</b></p>
    <p>p-content2</p>
    <panda>panda-content</panda>
    <div>div-content<span>span-content</span></div>
    """
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(text=re.compile('content$')))
    运行结果:
    ['panda-content', 'div-content', 'span-content']
5. 通过属性查找
如：print(soup.find_all(id='panda'))找id是panda的标签。
6. 限制个数
如：soup.find_all('p',limit=3)找前3个p标签。

find()
find_all()返回一个列表 
find()返回第一个结果

find_parent()
在当前元素的父节点中查找,返回第一个

find_parents()
在当前元素的父节点中查找,返回list

find_next_sibling()
在当前元素的兄弟节点中查找(弟弟),返回第一个

find_next_siblings()
在当前元素的兄弟节点中查找(弟弟),返回list

find_previous_sibling()
在当前元素的兄弟节点中查找(哥哥),返回第一个

find_previous_siblings()
在当前元素的兄弟节点中查找(哥哥),返回list

find_next()
在当前元素的相邻节点中查找(向下),返回第一个

find_all_next()
在当前元素的相邻节点中查找(向下),返回list

find_previous()
在当前元素的相邻节点中查找(向上),返回第一个

find_all_previous()
在当前元素的相邻节点中查找(向上),返回list

###########################################################################################
CSS选择器
1. 通过标签名查找
print(soup.select('p'))找p标签。
2. 通过类名查找
print(soup.select('.p-class'))找class为p-class的标签。
3. 通过 id 名查找
print(soup.select('#panda'))找id为panda的标签。
4. 组合查找
print(soup.select('div #panda'))找div下class为panda的标签。
5. 属性查找
soup.select('p[class="p-class"]')找class等于p-class的p标签。

'''






