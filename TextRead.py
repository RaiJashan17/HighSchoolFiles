#Jashan Rai
#Revised on 3/12/19
#TextRead.py

FileName=input("Enter the file name which you want to read (include the .txt part): ") #Asks for the file
Read=open(FileName,"r")
prt="1"
lines=Read.readlines() #This is where the lines will be read
while prt != 'input':
    n=int(input("Enter the line number you want to read: "))
    print(lines[n])
    prt=input("If you want to continue enter 1 but if your done type 0: ")
    if prt=="0":
        break

Read.close()
