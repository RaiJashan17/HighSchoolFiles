#Jashan Rai
#Revised on 3/12/2019
#TextSort.py

x=[] #Creates a Empty List

f=open('7oldsamr.txt','r') #This is where the code sorts the strings
for line in f:
    x=line.split()
    print (sorted(x, key=str.upper))
f.close
