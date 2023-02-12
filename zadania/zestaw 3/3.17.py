import math
def sys_trojkowy(liczba):
    wynik=0
    i=0
    while liczba>0:
        wynik= liczba%3 * 10**i+wynik
        liczba//=3
        i+=1
    return wynik

def czy_pierwsza(liczba):
    if liczba==2 or liczba==3:
        return True
    if liczba%2==0 or liczba%3==0 or liczba<2:
        return False
    i=5
    while i<int(math.sqrt(liczba))+1:
        if liczba%i==0:
            return False
        i+=2
        if liczba%i==0:
            return False
        i+=4
    return True

def suma(liczba,t1,t2):
    i=len(t1)-1
    suma=0
    while i>=0:
        if liczba%10==1:
            suma+=t1[i]
            suma+=t2[i]
        if liczba%10==2:
            suma+=t2[i]
        if liczba%10==0 or liczba==0:
            suma+=t1[i]
        liczba//=10
        i-=1
    return suma

# 0-t1, 1-obie, 2-t2
def fun(t1,t2):
    n=len(t1)
    tab=[]
    licznik=0

    for i in range(3**n): 
        mask=sys_trojkowy(i)
        sum=suma(mask,t1,t2)
        flaga=1
        for j in tab:
            if j==sum:
                flaga=0
        if flaga==1:
            tab.append(sum)
            print(sum)
            licznik+=1
    return licznik
        

t1 = [1,3,6]
t2 = [9,7,6]
print("licznik: ",fun(t1,t2))
