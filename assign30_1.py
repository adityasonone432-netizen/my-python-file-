
# total number of lines in files 
import sys
def Countline(fname):
    fobj=open(fname,"r")
    count=0

    for line in fobj:
        count+=1

    fobj.close()
    return count

def main():
    filename=sys.argv[1]
    Ret=Countline(filename)
    print("Total number of lines in ",filename,":", Ret)

if __name__ == "__main__":
    main()



    







