t=[1,2,3,6,8,9,4324,432,7,4,23,6,78,999,44]
def najdluzszy_podciag(t):
    dlugosc=1
    dlugosc_temp=1
    poprzedni = t[0]
    for i in t[1:]:
        if(poprzedni<i):
            dlugosc_temp+=1
        else:
            if(dlugosc_temp>dlugosc):
                dlugosc=dlugosc_temp
                dlugosc_temp=1
        poprzedni=i
    if dlugosc==1: #sprawdzenie przypadku że ciag najdluzszy jest na koncu
        return dlugosc_temp
    else:
        return dlugosc
print(t)
print(najdluzszy_podciag(t))