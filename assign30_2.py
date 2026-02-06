
# total number of Words in files 

import sys
def Countwords(fname):
    fobj=open(fname,"r")
    count=0

    for line in fobj:
        Words=line.split()
        count+= len(Words)
        

    fobj.close()
    return count 

def main():
    filename=sys.argv[1]
    Ret=Countwords(filename)
    print("Total number of lines in ",filename,":", Ret)

if __name__ == "__main__":
    main()



    







