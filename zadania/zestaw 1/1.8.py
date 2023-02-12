import math

flaga=1
liczba = int(input())
if liczba == 2 or liczba == 3:
    flaga = 1
elif liczba<=1 or (liczba % 2==0 and liczba != 2):
    flaga = 0 
i=4
while i <= math.sqrt(liczba):
    if liczba%i==0:
        flaga=0
        break
    i+=1

if flaga==1:
    print("Tak")
else:
    print("Nie")