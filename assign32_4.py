# duplicate delete excution time report

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

    start = time.time()

    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicateRemovalTime.py <DirectoryName>")
        return
    WriteLog("\n--------------Duplicate Removal  + Time Report :" + time.ctime()+ "-------")


    DeleteDuplicate(sys.argv[1])

    end = time.time()

    WriteLog("Execution Time : " + str(end - start))


if __name__ == "__main__":
    main()