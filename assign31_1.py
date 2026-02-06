# Display all file that extention
import sys
import os

def WriteLog(message):
    fobj = open("Log.txt", "a")
    fobj.write(message + "\n")
    fobj.close()

def ValidateInput(path, ext):
    if not os.path.exists(path):
        WriteLog("Directory does not exist")
        return False
    if not ext.startswith("."):
        WriteLog("Invalid extension")
        return False
    return True

def SearchFiles(path, ext):
    for file in os.listdir(path):
        if file.endswith(ext):
            WriteLog("Found File : " + file)

def main():
    try:
        if len(sys.argv) != 3:
            WriteLog("Invalid number of arguments")
            return

        directory = sys.argv[1]
        extension = sys.argv[2]

        if ValidateInput(directory, extension):
            SearchFiles(directory, extension)
            WriteLog("Search completed successfully")

    except Exception as e:
        WriteLog("Error occurred : " + str(e))

if __name__ == "__main__":
    main()