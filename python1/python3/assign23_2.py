# opps problem

class BankAccount:
    RIO=10.5

    def __init__(self,Name,Amount):
            self.Name=Name
            self.Amount=Amount

    def Display(self):
          print("account holder name:",self.Name)
          print("Current balance:",self.Amount)   
        
    
    def Deposite(self):
          amt=float(input("Enter deposite amount:"))
          self.Amount+=amt

    def Withdraw(self):
          amt=float(input("Enter Withdraw amount:")) 
          if amt<=self.Amount:   
             self.Amount-=amt
          else:
             print("Insfficient balance")

    def CalculaterInterest(self):
         Interest=(self.Amount*self.RIO)/100
         return Interest
    
    
    
obj1=BankAccount("Aditya sonone",10000)
obj2=BankAccount("Tanushri sharma ",5000)   

obj1.Deposite()
obj1.Withdraw()
print("Interest:",obj1.CalculaterInterest())
obj1.Display()


print("-----------------------------")


obj2.Deposite()
obj2.Withdraw()
print("Interest:",obj2.CalculaterInterest())
obj2.Display()