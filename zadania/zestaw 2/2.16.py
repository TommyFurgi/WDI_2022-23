def suma_cyfr(liczba):
    suma=0
    while liczba>0:
        suma+=liczba%10
        liczba//=10
    return suma


def czynniki_pierwsze(liczba):
    t=[]
    i=2
    while liczba!=1:
        if liczba%i==0:
            t.append(i)
            liczba//=i
            i=2
        else:
            i+=1
    return t

for i in range(2,100):
    sumacyfr=suma_cyfr(i)
    tab=czynniki_pierwsze(i)
    suma2=0
    for j in tab:
        suma2+=suma_cyfr(j)
    if suma2==sumacyfr:
        print(i)
