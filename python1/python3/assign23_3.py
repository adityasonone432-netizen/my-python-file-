#  class name numbers 
class Numbers:

    def __init__(self,value):
        self.value=value

    def Factors(self):
        factors=[]
        for i in range(1,self.value+1):
         if self.value%i == 0:
            factors.append(i)
        print("factors :",factors)
        return factors 
    def Sumfactors(self):
        factors=self.Factors()
        return sum(factors)-self.value   
    
    def Chkprime(self):
       if self.value <= 1:
          return False
       for i in range(2,int(self.value**0.5 )+1):
          if self.value % i == 0:
             return False
          return True
       
    def Chkperfect(self):
       return self.Sumfactors()==self.value
num=int(input("Enter first number:")) 

obj1=Numbers(num)
obj2=Numbers(num)

print("factors :",obj1.Factors())
print("sumfactors:",obj1.Sumfactors())
print("prime:",obj1.Chkprime())
print("perfect :",obj1.Chkperfect())

          
       


             
