# each example is independent.
# example 1 ######################################################################

# class后面紧接着是类名，即Oop，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Oop(object): #定义类
    # __init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self,index):
        self.index=index

    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
    # 但self不需要传，Python解释器自己会把实例变量传进去.
    def print_index(self):
        self.index+=1
        print(self.index)

index=3

# 创建类的实例.
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去
c=Oop(index)

c.print_index()#4
# self.index改变之后,外面的index的值并没有变.
print(index)#3
# 上次加1之后,变成了4,这次再次print,输出的是5.
c.print_index()#5

# 和静态语言不同，Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同.
c.name="c-name"
print(c.name)#c-name

b=Oop(index)
# 下面会报错.
# print(b.name)

# example 2 ######################################################################
# 访问限制.
class Student(object):
    def __init__(self, name, score):
        # 要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
        # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问.
        self.__name__="teshu"
        self.name=name
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s/%s: %s' % (self.name,self.__name, self.__score))#abc/abc: 100

c=Student("abc",100)
c.print_score()
print(c.name)#abc
#print(c.__name)#报错.
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量.
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
print("c._Student__name",c._Student__name)#c._Student__name abc

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
print(c.__name__)#teshu

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# example 3 ######################################################################
# 继承与多态

class Animal(object):
    def run(self):
        print('Animal is running...')

#继承.
class Dog(Animal):
    pass

class Cat(Animal):
    def run(self):
        print('cat is running...')

    def bask(self):
        print('cat is basking in the sun.')

dog=Dog()
dog.run()#Animal is running...

cat=Cat()
cat.run()#cat is running...
cat.bask()#cat is basking in the sun.

#多态.
print(isinstance(dog, Animal))#True
print(isinstance(dog, Dog))#True

animal=Animal()
print(isinstance(animal,Dog))#False

# 多态的好处例子.
# 只需要传入Animal类型,就可以执行相应的run.
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

# 新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
run_twice(Cat())
'''
Animal is running...
Animal is running...
cat is running...
cat is running...
'''

# example 4 ######################################################################

