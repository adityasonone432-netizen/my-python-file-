#  Arithmatic class and calculate Add sum div mul 
class Arithematic:
    
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self):
        self.value1=int(input("Enter the value1:"))
        self.value2=int(input("Enter the value2:"))

    def Addition(self):
        return self.value1 + self.value2
       

    def subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return  self.value1 * self.value2
    
    def Division(self):
        if self.value2 == 0:
            return "Division is not allowed "
        else:
            return self.value1 / self.value2
        
obj1=Arithematic()    
obj2=Arithematic()

obj1.Accept()
print("Addition is:",obj1.Addition())
print("Subtraction  is:",obj1.subtraction())
print("Multiplication is is:",obj1.Multiplication())
print("Division  is:",obj1.Division())

obj2.Accept()
print("Addition is:",obj2.Addition())
print("Subtraction  is:",obj2.subtraction())
print("Multiplication is is:",obj2.Multiplication())
print("Division  is:",obj2.Division())

