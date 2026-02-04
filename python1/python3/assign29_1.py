# Check File Existds in current Derectory
import os
Filename=input("Enter the File name:")
if os.path.isfile(Filename):
    print(f"{Filename} exists.")
else:
    print(f"{Filename} does not exists")
    