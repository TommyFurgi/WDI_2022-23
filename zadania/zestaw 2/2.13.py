liczba=int(input())
flaga=1

cyfra = liczba%10
liczba2= liczba//10
while liczba2 > 0:
    if liczba2%10==cyfra:
        flaga=0
        break
    liczba2 //=10
if(flaga==1):
    print("Jest zakonczona unikalna cyfra ")  