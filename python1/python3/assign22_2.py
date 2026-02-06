# circle class and calculate radius area and circumferance
class circle:
    PI=3.14
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0
    def Accept(self):
        self.radius=float(input("Enter the radius:"))

    def CalculateArea(self):
        self.area=circle.PI*self.radius*self.radius

    def Calculatecircumference(self):
        self.circumference=2*circle.PI*self.radius

    def Display(self):
        print("radius of :",self.radius)
        print("Area of :",self.area)
        print("Circumference of :",self.circumference)
obj1=circle()
obj2=circle()

obj1.Accept()
obj1.CalculateArea()
obj1.Calculatecircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.Calculatecircumference()
obj2.Display()



