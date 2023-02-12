def fun(tab):
    n=len(tab)
    for i in tab:
        p=0
        for j in i:
            if not czy_zawiera_parzysta(j):
                break
            else:
                p+=1
            if p==n:
                print(i)
                return True
    return False

def czy_zawiera_parzysta(liczba):
    while liczba>0:
        if liczba%2==0:
            return True
        liczba//=10
    return False

tab=[[15,1,77],[32,30,61],[33,71,1]]
print(fun(tab))