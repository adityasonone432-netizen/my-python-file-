# Display file contents 
Filename=input("Enter the Filename:")

fobj= open(Filename,"r")
data=fobj.read()
print(data)
fobj.close()


# mtd second 
filename=input("Enter the filename:")
try:
    fobj=open(filename,"r")
    print(fobj.read())
    fobj.close()
except:
    print("File not found ")
