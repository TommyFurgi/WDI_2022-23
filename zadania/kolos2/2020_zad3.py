'''
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi. Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
zwrócić położenie wież w postaci krotki (row1, col1, row2, col2).
Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
Przykładowe wywołania funkcji:
print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]] # (2,3,3,1) suma=35
'''

def sumuj(T,x1,y1,x2,y2):
    suma=0
    if x1==x2:
        for i in range(len(T)):
            suma+=T[x2][i]
            suma+=T[i][y1]
            suma+=T[i][y2]
        suma-=T[x1][y1]
        suma-=T[x2][y2]

    if y1==y2:
        for i in range(len(T)):
            suma+=T[x1][i]
            suma+=T[x2][i]
            suma+=T[i][y1]
        suma-=T[x1][y1]
        suma-=T[x2][y2]


    else:  
        for i in len(T):
            suma+=T[x1][i]
            suma+=T[x2][i]
            suma+=T[i][y1]
            suma+=T[i][y2]
        suma-=T[x1][y1]
        suma-=T[x1][y1]
        suma-=T[x2][y1]
        suma-=T[x1][y2]
    return suma


def chess(T):
    suma_najw=0
    suma=0
    a,b,c,d=0,0,0,0
    for i in range(len(T)):
        for j in range(len(T)):
            for m in range(len(T)):
                if m!=i:
                    for n in range(len(T)):
                        if n!=j:
                            suma=sumuj(T,i,j,m,n)
                            if suma>suma_najw:
                                suma_najw=suma
                                a,b,c,d=i,j,m,n
    return a,b,c,d

