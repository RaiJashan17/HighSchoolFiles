#Jashan Rai
#9/30/18
#Section 1
#population.py

"""This script will calculate the population of the US from present to five years in the future"""

Starting_Population=312032486
Births=(60/7)*60*24*365
Deaths=(60/13)*60*24*365
Immigration=(60/45)*60*24*365
print("Starting Population %.9d" % Starting_Population)
print("  Year 1 Population %.9d" % (Starting_Population+(Births*1)+(Immigration*1)-(Deaths*1)))
print("  Year 2 Population %.9d" % (Starting_Population+(Births*2)+(Immigration*2)-(Deaths*2)))
print("  Year 3 Population %.9d" % (Starting_Population+(Births*3)+(Immigration*3)-(Deaths*3)))
print("  Year 4 Population %.9d" % (Starting_Population+(Births*4)+(Immigration*4)-(Deaths*4)))
print("  Year 5 Population %.9d" % (Starting_Population+(Births*5)+(Immigration*5)-(Deaths*5)))
