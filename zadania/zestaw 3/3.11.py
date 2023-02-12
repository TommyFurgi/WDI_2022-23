def dl_ciagu(t):
    dlugosc=1
    dlugosc_temp=1
    poprzedni=t[0]
    q=t[1]/t[0]
    for i in t[1:]:
        if q==i/poprzedni:
            dlugosc_temp+=1
        else:
            if dlugosc_temp>dlugosc:
                dlugosc=dlugosc_temp
            dlugosc_temp=2
            q=i/poprzedni
        poprzedni=i
    if dlugosc_temp>dlugosc: #sprawdzenie przypadku że ciag najdluzszy jest na koncu
        return dlugosc_temp
    else: 
        return dlugosc

t=[3,6,12,24,2,8,32,2,4,8,16,32,64]
print(dl_ciagu(t))