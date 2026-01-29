# class name Book store
class Bookstrore:
    NoOfBooks=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        Bookstrore.NoOfBooks+=1
    def Display(self):
        print(f"{self.Name} by {self.Author}.No of Books:{Bookstrore.NoOfBooks} ")    


obj1=Bookstrore("Linux system programing","Robert Love")       
obj1.Display()

obj2=Bookstrore(" C programing","Dennis Ritchie")       
obj2.Display()

