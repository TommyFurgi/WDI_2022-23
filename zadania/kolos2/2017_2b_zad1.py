'''Zadanie 1.
Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
funkcja powinna zwróci¢ warto±¢ typu bool.'''

import math
def czy_pierwsza(liczba):
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

def fun(t):
    suma=0
    for i in range(len(t)):
        for j in range(len(t)):
            suma=t[i][j]
            for n,m in [(-1,2),(1,2),(2,1),(2,-1)]:
                if 0<=i+n<len(t) and 0<=j+m<len(t):
                    if czy_pierwsza(t[i][j]+t[i+n][j+m]):
                        return True

    return False