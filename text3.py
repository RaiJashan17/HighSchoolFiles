from random import randint
file=open("integers.txt","w")
for i in range(randint(1,10)):
    file.write("%d\n" % (i+1))
file.close()

f=open("integers.txt","r")
theSum=0
count=0
for line in f:
    wordlist=line.split()
    for word in wordlist:
        count=count+1
        number=int(word)
        theSum+=number

print(theSum/count)
