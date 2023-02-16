#Jashan Rai
#5/16/19
#Text Files Exercises

from os.path import exists

fileName=input("Enter a file name: ")

if not exists(fileName):
    print("Error: the file does not exist!")
else:
    inputFile=open(fileName, 'r')
    print(inputFile.read())
