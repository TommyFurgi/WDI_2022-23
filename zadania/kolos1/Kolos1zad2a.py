def ile_parzystych(liczba):
    licznik=0
    while liczba>0:
        if liczba%5==0 or liczba%5==2 or liczba%5==4:
            licznik+=1
        liczba//=5
    return licznik
    
def fun(tab1,tab2):
    t1=[[0 for _ in range(len(tab1))]for _ in range(len(tab1))]
    t2=[[0 for _ in range(len(tab2))]for _ in range(len(tab2))]