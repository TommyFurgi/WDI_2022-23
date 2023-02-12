def fun(tab): #sukamy najwiekszej kolumny i najmniejszego wiersza
    row_ujem=0
    row_dodat=0
    suma_row_dodat=10000000
    suma_row_ujem=-10000000
    p=0
    for i in tab: #wiersz
        suma=0
        for j in i:
            suma+=j
        if suma>suma_row_ujem and suma<0:
            row_ujem=p
            suma_row_ujem=suma
        if suma<suma_row_dodat and suma>0:
            row_dodat=p
            suma_row_dodat=suma
        p+=1
    col_dodat=0
    col_ujem=0
    suma_col_dodat=0
    suma_col_ujem=0
    i=0
    while i<len(tab): #kolumna
        suma=0
        j=0
        while j<len(tab):
            suma+=tab[j][i]
            j+=1
        if suma>suma_col_ujem:
            col_ujem=i
            suma_col_ujem=suma
        if suma>suma_col_dodat:
            col_dodat=i
            suma_col_dodat=suma
        i+=1
    return #nie ma sensu

tab=[[1,2,3],[4,5,6],[7,8,9]]
for i in tab:
    print(i)
print(fun(tab))