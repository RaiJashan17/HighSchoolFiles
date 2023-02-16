#Jashan Rai
#Period 1
#text1.py

from random import randint
file=open("myfile.txt","w")
for i in range(randint(1,100)):
    file.write("This is line number %d\n" % (i+1))
file.close()

fileread=open("myfile.txt","r")
count=0
for line in fileread:
    count=count+1
print("Line Count:", count)
