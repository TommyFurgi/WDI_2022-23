'''Zadanie 1.
Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦) wypeªniona liczbami naturalnymi. Na szachownicy
znajduj¡ si¦ dwie wie»e. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie: czy istnieje ruch wie»¡
zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach? Do funkcji nale»y przekaza¢ tablic¦ oraz
poªo»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
Uwaga: zakªadamy, »e wie»a szachuje caªy wiersz i kolumn¦ z wyª¡czeniem pola, na którym stoi.'''
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

def fun(T,x1,y1,x2,y2):
    suma=sumuj(T,x1,y1,x2,y2)
    for i in range(-len(T),len(T)):
        if 0<=i+x1<len(T):
             if sumuj(T,x1+i,y1,x2,y2)>suma:
                return True

        if 0<=i+x2<len(T):
             if sumuj(T,x1,y1,x2+i,y2)>suma:
                return True

        if 0<=i+y2<len(T):
             if sumuj(T,x1,y1,x2,y2+i)>suma:
                return True

        if 0<=i+y1<len(T):
             if sumuj(T,x1,y1+i,x2,y2)>suma:
                return True

    return False