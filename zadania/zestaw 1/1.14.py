def silnia(n):
    wynik=1
    for i in range(1,n+1):
        wynik*=i
    return wynik

potega=0
x=1.57
print(x**0)
wynik=0
for i in range(50):
    if potega%4==0:
        wynik+=(x**potega)/silnia(potega)
    else:
        wynik-=(x**potega)/silnia(potega)
    potega+=2

print(wynik)