'''
網易雲課程：《瘋狂的python：快速入門精講》略略略😀

😋😑😆
'''

print('''
《英雄无敌》之英雄降临
1. 开局玩家起名字。
2. 列表初始化为英雄属性、名字、血值、攻击力、防御力。
3. 判断名字是否为空，默认为“玩家一”。
4. 判断英雄行动方向。
''')
print('''
    ***
    Hero is me! Welcome to visit my world!
    You must obey my world\'s rules, or you will be expelled~~
    ***
    ''')
#name = input('input your name:')
name='princess'

if not name:#name为假，name如果没有值就是假，否则为真
    name='little cute guy'
    print('''
    ***
    I let you off easy for your insubordination this time!!! 
    Your name is specified as \'little cute guy\'.
    ***
''')

hp=100
visitorList=[name,hp]

print("your name:",visitorList[0],",your hp:",visitorList[1])

print("\n切片name[0:1],看看有那些字符被输出了：",name[0:1])

print("\n列表解析")
print('''
    ***
    Now I will give you a mathematical problem:
    please print all the natural numbers no more than 100 that can be mutiples of 3 or 5, and compute the sum of all the number.
    ***
''')

nums = []
for i in range(1,100):
    if i%3==0 or i%5:
        nums.append(i)
print('all the nums have been stored in the list \'nums\':',nums)

print('sum函数，你给它一个列表可以自动求和,sum(nums)=',sum(nums))

print('''
   ***
   but you can use list comprehensions:
   在需要改变列表而不是需要新建某列表时，可以用列表解析；
   列表解析的表达式为：
       [expr for iter_var in iterable]
       [expr for iter_var in iterable if cond_expr]
   ***
''')

#[i*10 for i in range(10)]

#sum函数总用不了。。。TypeError: 'int' object is not callable
#之後試又能用了，可能是上次用的時候定義過sum變量，雖然這個sum變量在運行sum函數的時候已經刪掉了，但是好像仍然對程序產生了影響。
print(sum([i for i in range(10) if i%3==0 or i%5 ==0]))



print("\nopen a file , open('this.log','w'),this file is in SpiderFiles")
open('this.log','w')
open('this.log','w').write('abc')
name2='adddd'
print('\nname2 is:%s'%name2)

import os

if os.path.isfile('this.log'):
    print('this.log file exists\n')
