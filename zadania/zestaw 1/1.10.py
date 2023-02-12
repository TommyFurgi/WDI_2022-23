import math

liczba = 2
while liczba<1000000:
    suma=1
    i=2
    while i<=math.sqrt(liczba):
        if liczba%i==0:
            suma+=i
            if i**2 != liczba:
                suma+=int(liczba/i)
        i+=1
    if suma == liczba:
        print("Doskonala: ", liczba)
    liczba+=1