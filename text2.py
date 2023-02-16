#Jashan Rai
#2/6/19
#Text Files Exercises

file=open("email.txt","w")

file.write("Emails Found \n")
file.write("From JoeBob@gmail.com \n")
file.write("From KingArthur@yahoo.com \n")
file.write("From GaryGarot@gmail.com \n")
file.write("From SleepForToday@aol.com \n")

file.close()

count=0
file=open("email.txt","r")
for line in file:
    if line.startswith("From") :
        count=count+1

print(count)
