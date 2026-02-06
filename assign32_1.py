#  Display checksum of all files 

import os
import sys
import hashlib


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


def DirectoryChecksum(DirectoryName):

    if not os.path.isdir(DirectoryName):
        WriteLog("Invalid Directory")
        return

    for FolderName, SubFolderName, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            path = os.path.join(FolderName, fname)
            checksum = CalculateCheckSum(path)
            WriteLog(path + " -> " + checksum)


def main():

    

    if len(sys.argv) != 2:
        print("Usage : DirectoryChecksum.py <DirectoryName>")
        return
    WriteLog("\n--------------Checksum Report--------")
    DirectoryChecksum(sys.argv[1])


if __name__== "__main__":
    main()