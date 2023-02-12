def fun(tab):
    najw=tab[0]
    najm=tab[0]
    flaga_najw=True
    flaga_najm=True
    for i in tab:
        if i>najw:
            najw=i
            flaga_najw=True
        elif najw==i:
            flaga_najw=False
        elif i<najm:
            najm=i
            flaga_najm=True
        elif najm==i:
            flaga_najm=False
    print(najw, najm)
    return flaga_najm and flaga_najw

tab=[1,2,3,1,5,5]
print(fun(tab))