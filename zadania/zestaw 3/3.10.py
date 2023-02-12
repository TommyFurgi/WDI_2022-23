def dlugosc_ciagu(t):
    dlugosc=1
    dlugosc_temp=1
    poprzedni=t[0]
    r=t[1]-poprzedni
    for i in t[1:]:
        if i-poprzedni==r:
            dlugosc_temp+=1
        else:
            if dlugosc_temp>dlugosc:
                dlugosc=dlugosc_temp
            dlugosc_temp=2
            r=i-poprzedni
        poprzedni=i

    if dlugosc_temp>dlugosc: #sprawdzenie przypadku że ciag najdluzszy jest na koncu
        return dlugosc_temp
    else:
        return dlugosc
    
t=[1,3,5,7,8,10,12,13,4,8,12,16,20,24,28,35]
print(dlugosc_ciagu(t))