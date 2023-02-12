def dlugosc_tab(t): 
    licznik=0 
    for _ in t:
        licznik+=1
    return licznik

def sprawdz(T):
    dl=dlugosc_tab(T)
    T2=[False]*dl
    T2[0]=True
    for i in range(dl):
        if T2[i]==True:
            temp=T[i]
            k=2
            while temp != 0:
                while temp%k==0:
                    if k+i<dl:
                        T2[k+i]=True
                    temp=temp//k
                k+=1
            
    return T2[dl-1]


    
t=[10,56,432,6363,634535,5435,655,534,666,534,110]

print(sprawdz(t))