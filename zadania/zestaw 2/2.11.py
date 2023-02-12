liczba = int(input())
reszta1=liczba%10
liczba//=10
flaga=1
while liczba>0:
    reszta2= liczba%10
    liczba//=10
    if reszta1<=reszta2:
        flaga=0
        break
    reszta1 = reszta2

if flaga==1:
    print("cyfry tworza ciag rosnacy")