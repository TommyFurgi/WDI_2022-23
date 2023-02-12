import math
def czy_pierwsza(liczba): 
    if liczba == 2 or liczba == 3:
        return True
    if liczba %2 == 0 or liczba%3==0 or liczba<=1:
        return False
    i=5
    while int(math.sqrt(liczba))+1>i:
        if liczba%i == 0:
            return False
        i+=2
        if liczba%i == 0:
            return False
        i+=4
    return True

def fun(l,result=0,pos=0,b=False):
    if l==0:
        if czy_pierwsza(result) and b and result>9:
            print(result)
        return
    fun(l//10,result,pos,True)
    fun(l//10,result+((l%10) * 10**pos),pos+1,b)


fun(4567235234524)
