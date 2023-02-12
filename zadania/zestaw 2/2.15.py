def dl(liczba):
    licznik=0
    while liczba>0:
        licznik+=1
        liczba//=10
    return licznik
i=1
while True:
    suma=0
    p=i
    dlugosc=dl(i)
    while p>0:
        suma+=(p%10) ** dlugosc
        p//=10
        if suma>i:
            break

    if i==suma:
        print(i)
    i+=1