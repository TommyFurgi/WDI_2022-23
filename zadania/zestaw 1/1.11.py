import math

liczba=2
while liczba < 1000000:
    suma1 = 1
    i = 2
    while i<=math.sqrt(liczba):
        if liczba%i==0:
            suma1+=i
            if i**2 != liczba:
                suma1+=int(liczba/i)
        i+=1
    i=2
    suma2=1
    while i<=math.sqrt(suma1):
        if suma1%i==0:
            suma2+=i
            if i**2 != suma1:
                suma2+=int(suma1/i)
        i+=1
    if suma2 == liczba and suma1 < suma2:
        print(suma1, suma2)
    liczba+=1