#  Directory duplicate removal 

import os
import sys
import hashlib
import time 


def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()


def CalculateCheckSum(FileName):

    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def DeleteDuplicate(DirectoryName):

    Duplicate = {}

    for FolderName, SubFolderName, FileNames in os.walk(DirectoryName):

        for fname in FileNames:
            path = os.path.join(FolderName, fname)
            checksum = CalculateCheckSum(path)

            if checksum in Duplicate:
                os.remove(path)
                WriteLog("Deleted : " + path)
            else:
                Duplicate[checksum] = path


def main():

    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicateRemoval.py <DirectoryName>")
        return
    WriteLog("\n--------------Duplicate Removal Report :" + time.ctime()+ "-------")


    DeleteDuplicate(sys.argv[1])


if __name__== "__main__":
    main()