def fun(t):
    n=len(t)
    j=1
    suma=t[0]
    suma_indeksow=0
    dl=1
    dl_podciag=0
    while j<n: #pierwsza petla- od ktorego indeksu zaczynymay sprawdzac
        i=j
        while i<n:
            if t[i-1]<t[i]: #sprawdzenie czy rosnacy
                suma_indeksow+=i
                suma+=t[i]
                dl+=1
                if suma==suma_indeksow: #sprawdzenie sumy
                    dl_podciag=max(dl,dl_podciag)
            else:
                suma_indeksow=i #jak nie rosnacy
                suma=t[i]
                dl=1
            i+=1
        suma_indeksow=j
        suma=t[j]
        dl=1
        j+=1
    return dl_podciag

t=[4,1,2,0,4,8]
print(fun(t))