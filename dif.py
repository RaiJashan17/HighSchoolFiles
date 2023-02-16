#Jashan Rai
#Revised on 3/12/2019
#dif.py

filex=[] #Creates empty list
filey=[]

x=input("Enter the first file you want to compare: ") #Asks for the files
y=input("Enter the second file you want to compare: ")
line=int(input("Which line would you like to compare: "))

f=open(x,'r') #Reads first file contents
lines=f.readlines()
linex=lines[line]
filex+=linex.split()
f.close()

f=open(y,'r') #Reads second file contents
lines=f.readlines()
liney=lines[line]
filey+=liney.split()
f.close()

if filex==filey: #Checks if their equal and prints the result
    print("Yes these lines contain the same content.")
if filex!=filey:
    print("No these lines contain different content.")
print(linex)
print(liney)
