# copy all file for specific exetention first directory to second directory
import os 
import sys
import shutil

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def CopyExt(src, dst, ext):
    if not os.path.exists(dst):
        os.mkdir(dst)

    for file in os.listdir(src):
        if file.endswith(ext):
            s = os.path.join(src, file)
            d = os.path.join(dst, file)
            shutil.copy(s, d)
            WriteLog("Copied : " + file)

def main():
    try:
        WriteLog("----------copy all file for specific exetention first directory to second directory----------")
        
        if len(sys.argv) != 4:
            WriteLog("Invalid arguments")
            return

        src = sys.argv[1]
        dst = sys.argv[2]
        ext = sys.argv[3]

        if not os.path.exists(src):
            WriteLog("Source directory not found")
            return

        if not ext.startswith("."):
            WriteLog("Invalid extension")
            return

        CopyExt(src, dst, ext)
        WriteLog("Copy with extension completed")

    except Exception as e:
        WriteLog("Error : " + str(e))

if __name__== "__main__":
    main()