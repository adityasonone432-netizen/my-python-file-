#  copy files to another 
import os 
import sys

import os
import sys
import shutil

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def CopyAll(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)

    for file in os.listdir(src):
        s = os.path.join(src, file)
        d = os.path.join(dst, file)
        if os.path.isfile(s):
            shutil.copy(s, d)
            WriteLog("Copied : " + file)

def main():
    try:
        WriteLog("----------copy all files from first directory to second directory--------")
        
        if len(sys.argv) != 3:
            WriteLog("Invalid arguments")
            return

        src = sys.argv[1]
        dst = sys.argv[2]

        if not os.path.exists(src):
            WriteLog("Source directory not found")
            return

        CopyAll(src, dst)
        WriteLog("Copy completed")

    except Exception as e:
        WriteLog("Error : " + str(e))

if __name__ == "__main__":
    main()