# copy file content into new file
import sys


fobj=sys.argv[1]    # ABC.txt
dest="Demo.txt"      #  given file

obj=open(fobj,"r")
data=obj.read()
obj.close()

dst=open(dest,"w")    # overwrite allowed
dst.write(data)
dst.close()

print("Content copied from ABC.txt to Demo.txt")

