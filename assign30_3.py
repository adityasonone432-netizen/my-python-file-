import sys
def DisplayContents(fname):
    fobj=open(fname,"r")

    for line in fobj:
        print(line,end="")

    fobj.close()
def main():
    fname=sys.argv[1]
    DisplayContents(fname)
    


if __name__ == "__main__":
    main()    