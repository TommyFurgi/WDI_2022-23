from random import randint

def fun(tab):
    i=0
    dl=0
    najdluzszy=0
    while i<len(tab):
        j=i+1
        while j<len(tab):
            if tab[i]==tab[j]:
                dl+=1
                p=1
                while True and i+p<len(tab) and i+p<j+p:
                    if tab[i+p]==tab[j-p]:
                        dl+=1
                        p+=1
                    else:
                        najdluzszy=max(najdluzszy,dl)
                        dl=0
                        break
            j+=1
        i+=1
    return max(najdluzszy,dl)


tab=[randint(100,999) for _ in range(1000)]
print(tab)
print(fun(tab))
