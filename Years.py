#Jashan Rai
#9/18/18
#Section #1
#"Years.py"

#This equation will convert minutes and convert them to years and days

Minutes=float(input("Enter the number of minutes: "))
Year=365
D=(60*24)
Day=Minutes/(D)
Years=Day//Year
Remaining_Days=Day%365
#Days=(Minutes-(Years*(D*Year)))//D
print("%.0d" % Minutes, "minutes is approximately %.0d" % Years, "years and %.0d" % Remaining_Days, "days.")
