'''
網易云課堂學習筆記
http://study.163.com/course/courseLearn.htm?courseId=1004933008#/learn/video?lessonId=1050679945&courseId=1004933008

C:\Users\oakpa\Desktop\test.html的内容。
<body>  
body here  
    <div class="c">class="c"</div>  
    <div id="i">id="i"</div>  
    <div>div</div>  
</body>  
'''

#使用lxml的示例。  
from lxml import etree  

html=etree.parse(r'C:\Users\oakpa\Desktop\test.html')#etree.parse()里面写的是文件名，它可以生成etree对象。  
print(type(html))#打印了一个etree的对象类型。  
  
result=html.xpath('//div')#获取所有div标签。/代表根路径，//代表所有根路径下的后代。  
print(result)#输出etree对象的列表。  
print(len(result))#输出结果的长度。  
print(type(result))#结果的类型。  
print(type(result[0]))#结果的第一个元素的类型。  
  
''''' 
输出： 
<class 'lxml.etree._ElementTree'> 
[<Element div at 0x18777f5df48>, <Element div at 0x18777f5df08>, <Element div at 0x18777f5dbc8>] 
3 
<class 'list'> 
<class 'lxml.etree._Element'> 
'''  
  
result=html.xpath('//div/@class')#获取div标签的所有class属性，@表示获取属性。  
print(result)  
''''' 
輸出: 
['c'] 
'''  
  
result=html.xpath('//div[@id="i"]')#所有id等於i的div標簽.  
print(result)  
print(result[0].text)  
''''' 
輸出: 
[<Element div at 0x255e9b19408>] 
id="i" 
'''  
  
result=html.xpath('//body//div')#找body下的所有div標簽.如果用//body/div找到是body的兒子中的div.  
  
result=html.xpath('//body')  
print(result[0].text)#注意.text衹能取出一級標簽下的所有内容.  
''''' 
輸出: 
body here 
'''  
  
result=html.xpath('//body//@class')#body自身及所有後代中的class.  
print(result)  
result=html.xpath('//body/@class')#body的class.  
print(result)  
''''' 
輸出: 
['c'] 
[] 
'''  
  
result=html.xpath('//body//div[last()-2]/@class')#獲取倒數第三個div的class.  
print(result)  
''''' 
輸出: 
['c'] 
'''  
  
result=html.xpath('//*[@class="c"]')#*代表所有標簽.獲取class為c的所有標簽.  
#再輸出標簽名.  
for i in result:  
    print(i.tag)  
''''' 
輸出: 
div 
'''  
