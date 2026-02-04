import sys
filename=sys.argv[1]
word=sys.argv[2]

f1=open(filename,"r")
data=f1.read()
f1.close()

count=data.count(word)
print(count)
