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






