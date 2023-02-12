def fun(tab): #sukamy najwiekszej kolumny i najmniejszego wiersza
    row=0
    suma_row=100000
    p=0
    for i in tab: #wiersz
        suma=0
        for j in i:
            suma+=j
        if suma<suma_row:
            row=p
            suma_row=suma
        p+=1
    col=0
    suma_col=0
    i=0
    while i<len(tab): #kolumna
        suma=0
        j=0
        while j<len(tab):
            suma+=tab[j][i]
            j+=1
        if suma>suma_col:
            col=i
            suma_col=suma
        i+=1
    return row,col

tab=[[1,2,3],[4,5,6],[7,8,9]]
for i in tab:
    print(i)
print(fun(tab))