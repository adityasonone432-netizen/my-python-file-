#copy content file into another file 
import sys

def CopyFile(first,second):
    f1first=open(first,"r")
    f2second=open(second,"w")

    for line in f1first:
        f2second.write(line)

    f1first.close()
    f2second.close()   


def main():
    fst=sys.argv[1]
    sec=sys.argv[2]
    CopyFile(fst,sec)
    print("copied file successfully")

if __name__ == "__main__":
    main()

