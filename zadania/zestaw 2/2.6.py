import math
liczba = int(input())
i=1
dzielnik=1
while i <= math.sqrt(liczba):
    if liczba%i==0:
        dzielnik = i
    i+=1
print(dzielnik, liczba//dzielnik)