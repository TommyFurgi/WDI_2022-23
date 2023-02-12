liczba=int(input())
flaga=0

dlugosc=0
liczba2=liczba
while liczba2>0:
    dlugosc += 1
    liczba2//=10 


liczba2=liczba
while liczba2>0:
    if liczba2%10==dlugosc:
        flaga=1
        break
    liczba2//=10

if flaga == 1:
    print("liczba zawiera liczbe rowna jej dlugosci ")
