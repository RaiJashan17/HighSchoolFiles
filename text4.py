#Jashan Rai
#2/8/2019
#Text Files Exercises

import os
currentDirectoryPath=os.getcwd()
ListOfFileNames=os.listdir(currentDirectoryPath)
for name in ListOfFileNames:
    print(name)
