import math

liczba = int(input())
i=1
while i <= math.sqrt(liczba):
    if liczba%i==0:
        print(i)
        if i**2 != liczba:
            print(int(liczba/i))
    i+=1    