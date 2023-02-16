#Jashan Rai
#Started on 3/12/2019
#DecimaltoRep.py

def DecimaltoRep(n,base):
    convertString="0123456789ABCDEF"

    if n<base:
        return convertString[n]
    else:
        return DecimaltoRep(n//base, base)+convertString[n%base]

if __name__=='__main__':
    print("Integer: 10, Base: 10, Conversion:",DecimaltoRep(10,10))
    print("Integer: 10, Base: 8, Conversion:",DecimaltoRep(10,8))
    print("Integer: 10, Base: 2, Conversion:",DecimaltoRep(10,2))
    print("Integers: 10, Base: 16, Conversion:",DecimaltoRep(10,16))
