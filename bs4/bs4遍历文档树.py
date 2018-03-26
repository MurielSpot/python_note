
'''
遍历文档树

节点内容
.string 属性
获取tag的文本内容 
如果tag只有一个 NavigableString类型子节点,那么这个tag可以使用 .string 得到子节点内容 
如果超过一个, 返回None

多个内容
.strings 属性 获取所有内容, 返回一个generator(包括空白字符) 
.stripped_strings 属性 获取所有内容, 返回一个generator(去除空白字符)

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
'''
