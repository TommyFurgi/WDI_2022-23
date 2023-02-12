import math
def dlugosc(liczba): #dlugosc liczby = len(str(liczba)) // log10(liczba)+1
    licznik=0
    while liczba > 0:
        licznik+=1
        liczba//10
    return licznik

def reverse(liczba): #odwaraca liczbe = str(liczba[::-1]) 2.3.py
    liczba2=0
    while liczba>0:
        liczba2=liczba2*10+liczba%10
        liczba=liczba//10
    return liczba2

def czy_pierwsza(liczba): #liczby pierwsze - najlepszy sposób
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

def nwd(a,b):
    while b:
        a, b = b, a%b
    return a

#sito eratostenesa
n=100
skr = [False] * (n + 1) #tworzymy tablice wypełnioną wartoscimai flase
i = 2
while i * i <= n:
    if  not skr[i]:
        j = i * i            
        while j <= n:
            skr[j] = True #wieloktortnosci i*i wypełaniamy my True
            j += i
    i += 1
for i in range(2, n+1):
    if not skr[i]: #jeśli false to wyswietl indeks
        print(i, end = " ")


#zamiana na binarny
def bin(liczba):
    wynik=0
    i=0
    while liczba>0:
        reszta=liczba%2
        wynik=reszta*10**i+wynik
        liczba//=2
        i+=1
    return wynik
print(bin(25))


