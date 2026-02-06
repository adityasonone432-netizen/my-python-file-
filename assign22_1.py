# python program  to implement a class a Demo 
class Demo :
    value=10     # class variable    (common for all object)

    def  __init__(self,a,b):
        self.No1=a       # instacce variable object specific 
        self.No2=b

    def fun(self):     # function or method
        print(self.No1,self.No2)    


    def gun(self):
        print(self.No1,self.No2)

obj1=Demo(11,21)      # object 1 created
obj2=Demo(51,101)     # object 2 created

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()