def sortuj(tab):
    while True:
        zamiana=False
        i=0
        while i<len(tab)-1:
            if tab[i]>tab[i+1]:
                zamiana=True
                tab[i],tab[i+1]=tab[i+1],tab[i]
            i+=1
        if zamiana==False:
            return tab

def sortuj2(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]

    return tab

t=[5,7,9,10,1]
print(sortuj2(t))