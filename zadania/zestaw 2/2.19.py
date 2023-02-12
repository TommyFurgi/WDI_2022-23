def fun(a,b):
    reszta=a%b
    tab=[False]*b
    while True:
        if tab[reszta*10%b]==True:
            indeks=reszta%b
            break
        else:
            tab[reszta*10%b]=True
        reszta=reszta*10%b
    wynik=str(a//b)+"."
    reszta=a%b
    flaga=0
    print(indeks)
    while True:
        if reszta==indeks:
            if flaga==0:
                wynik=wynik+"("+str(reszta*10//b)
                flaga=1
            else:
                wynik=wynik+")"
                break   
        else:
            wynik=wynik+str(reszta*10//b)
        reszta=reszta*10%b
    return wynik
print(fun(1,7))