from random import randint

def fun(tab):
    n=len(tab)
    dl=1
    dodatni=0
    ujemny=0
    r=0
    poprzedni=tab[0]
    i=1
    while i<n:
        if r==0:
            r=tab[i]-poprzedni
        if tab[i]-poprzedni==r:
            dl+=1
        else:
            if r>0:
                dodatni=max(dodatni,dl)
            elif r<0:
                ujemny=max(ujemny,dl)
            dl=1
            r=0
        poprzedni=tab[i]
        i+=1
    if r>0:
        dodatni=max(dodatni,dl) 
    else:
        ujemny=max(ujemny,dl)

    return dodatni-ujemny
        
    

tab=[randint(1,99) for _ in range(100)]
print(tab)
print(fun(tab))