#Jashan Rai
#Revised on 3/8/19
#Stats.py

import statistics #Import the module

print("Enter set of numbers to calculate.")  #Set the rules for typing in numbers
print("To stop entering number type STOP in all caps and then press answer.")
var = True
data=[]

while (var== True):
    num=input("Enter number or STOP: ") #Asks for numbers
    if(num=="STOP"):
        var = False
        break
    else:
        num=int(num)
        data.append(num)
print("Your input list is: ")
print(data)
print()

def mean(x): #Calculates the mean
    sm=sum(x[0:len(x)])
    mean=(sm/len(data))
    print(mean)

def median(x): #Calculates the median
   print(statistics.median(x))

def mode(x): #Calculates the mode
   print(statistics.mode(x))

if (sum(data[0:len(data)]))>0: #If there are numbers in the list it will print the stats
    print("mean")
    mean(data)
    print("median")
    median(data)
    print("mode")
    mode(data)

else:
    print("mean")
    print(0) #If there is no numbers in the list it will print 0
    print("median")
    print(0)
    print("mode")
    print(0)
