def czy_jest_nieparzysta(liczba):
    while liczba>0:
        if liczba%2==0:
            return False
        liczba//=10
    return True

def fun(tab):
    for i in tab:
        flaga=0
        for j in i:
            if  czy_jest_nieparzysta(j):
                flaga=1
                break
        if flaga==0:
            return False
    return True
                

tab=[[15,66,78],[22,33,6]]
print(fun(tab))