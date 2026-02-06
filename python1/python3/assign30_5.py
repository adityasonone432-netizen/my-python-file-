# search a word in line 
import sys
def SearchWords(fname,word):
    fobj=open(fname,"r")
    data=fobj.read()
    fobj.close()

    if word in data:
        return True
    else:
        return False
    
def main():
    filename=sys.argv[1]
    word=sys.argv[2]
    Ret=SearchWords(filename,word)

    if Ret == True:
        print("Words",word,"is found in ",filename)
    else:
        print("Words",word,"not  found in ",filename)


if __name__ == "__main__":
    main()
