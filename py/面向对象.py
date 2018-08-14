# each example is independent.
# example 1 ######################################################################
class oop():
    def __init__(self,index):
        self.index=index

    def print_index(self):
        self.index+=1
        print(self.index)

index=3
c=oop(index)

c.print_index()#4
# self.index改变之后,外面的index的值并没有变.
print(index)#3
# 上次加1之后,变成了4,这次再次print,输出的是5.
c.print_index()#5

# example 2 ######################################################################






