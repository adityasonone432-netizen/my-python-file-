#Dislpay grade
marks=int(input("Enter the number :"))
if marks>=75:
    print("Distiction")
elif marks>=60:
    print("first class")
elif marks>=50:
    print("second class")
else:
    print("fails")




# in labda function
def grade_marks(marks):
  if marks>=75:
    return "Distiction"
  elif marks>=60:
    return "first class"
  elif marks>=50:
    return "second class"
  else:
    return "fails"
marks=int(input("Enter the number :")) 
print("Grade:",grade_marks(marks))