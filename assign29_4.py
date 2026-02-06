# compare two files through command line 

import sys

file1=sys.argv[1]
file2=sys.argv[2]

f1=open(file1,"r")
data1=f1.read()
f1.close()

f2=open(file2,"r")
data2=f2.read()
f2.close()

if data1 == data2:
    print("success")
else:
    print("failure")
    