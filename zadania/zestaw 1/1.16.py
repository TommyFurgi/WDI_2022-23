licznik_koncwy=0
wyraz_poczatkowy=0
for i in range(2,10001):
    a=i
    licznik=0
    while a!=1:
        a=(a%2)*(3*a+1)+(1-a%2)*(a/2)
        licznik+=1
    if licznik>licznik_koncwy:
        licznik_koncwy=licznik
        wyraz_poczatkowy=i

print(wyraz_poczatkowy)

