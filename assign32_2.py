# Directory Duplicate check 

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


def FindDuplicate(DirectoryName):

    Duplicate = {}

    for FolderName, SubFolderName, FileNames in os.walk(DirectoryName):

        for fname in FileNames:
            path = os.path.join(FolderName, fname)
            checksum = CalculateCheckSum(path)

            if checksum in Duplicate:
                Duplicate[checksum].append(path)
            else:
                Duplicate[checksum] = [path]

    return Duplicate


def main():

    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicate.py <DirectoryName>")
        return
    
    WriteLog("\n--------------Duplicate File Report:" + time.ctime() + "-------")

    DirectoryName = sys.argv[1]

    data = FindDuplicate(DirectoryName)

    for value in data.values():
        if len(value) > 1:
            WriteLog("Duplicate Files:")
            for file in value:
                WriteLog(file)


if __name__ == "__main__":
    main()