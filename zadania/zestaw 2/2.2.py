def podziel(a,b,n):
    wynik = float(a)/float(b)
    przecinek = len(str(a//b))#ilosc cyfer przed przecinkiem
    wynik = str(wynik)
    return wynik[:przecinek+1+n]

print(podziel(2137,6,4))
print(2137/6)

#drugi sposób - petlami
liczba=int(input())
dzielnik=int(input())
n=int(input())
i=0
wynik='0'


wynik = str(liczba//dzielnik)
reszta = liczba%dzielnik
if reszta>0:
    wynik+="."

while i!=n:
    if reszta == 0:
        break
    wynik+=str(reszta*10//dzielnik)
    reszta = reszta*10%dzielnik
    i+=1

print(wynik)

