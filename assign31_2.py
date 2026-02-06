# Directory Rename ext1 to ext2 
import sys
import os 

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def Validate(path, ext1, ext2):
    if not os.path.exists(path):
        WriteLog("Directory not found")
        return False
    if not ext1.startswith(".") or not ext2.startswith("."):
        WriteLog("Invalid extension")
        return False
    return True

def RenameFiles(path, ext1, ext2):
    for file in os.listdir(path):
        if file.endswith(ext1):
            old = os.path.join(path, file)
            new = os.path.join(path, file.replace(ext1, ext2))
            os.rename(old, new)
            WriteLog("Renamed : " + file)

def main():
    try:
        WriteLog("---------Directory Rename Started---------")
        if len(sys.argv) != 4:
            WriteLog("Invalid arguments")
            return

        d = sys.argv[1]
        e1 = sys.argv[2]
        e2 = sys.argv[3]

        if Validate(d, e1, e2):
            RenameFiles(d, e1, e2)
            WriteLog("Rename completed")

    except Exception as e:
        WriteLog("Error : " + str(e))

if __name__ == "__main__":
    main()      
