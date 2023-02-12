'''1. Dwie liczby są zgodne siódemkowo, jeżeli posiadają tyle samo cyfr nieparzystych w ich reprezentacjach w systemie
pozycyjnym o podstawie 7. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 >= 1).
Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie umieszczenie tab1 wewnątrz tab2, aby w
pokrywającym się obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych
siódemkowo. '''


def warunek(n):
    licz=0
    while n>0:
        if n%7==5 or n%7==3 or n%7==1:
            licz+=1
        n//=10
    return licz

def fun(t1,t2):
    for i in range(len(t2)-len(t1)+1): 
        for j in range(len(t2)-len(t1)+1): 
            licznik=0
            for x in range(len(t1)):
                for y in range(len(t1)):
                    if warunek(t1[x][y])==warunek(t2[x+i][j+i]):
                        licznik+=1
            if licznik/(len(t1)**2) >= 0.33:
                return True
    return False