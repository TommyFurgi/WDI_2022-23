def ile_jedynek(liczba):
    licznik=0
    while liczba>0:
        if liczba%2==1:
            licznik+=1
        liczba//=2
    return licznik

def fun(T1,T2):
    n1=len(T1)
    n2=len(T2)
    t1=[[0 for _ in range(len(T1))] for _ in range(len(T1))]
    t2=[[0 for _ in range(len(T2))] for _ in range(len(T2))]

    for i in range(len(t1)):
        for j in range(len(t1)):
            t1[i][j]=ile_jedynek(T1[i][j])

    for i in range(len(t2)):
        for j in range(len(t2)):
            t2[i][j]=ile_jedynek(T2[i][j])

    najw=0
    for i in range(n2-n1+1):
        for j in range(n2-n1+1):
            licznik=0
            for x in range(n1):
                for y in range(n1):
                    if t2[i][j]==t1[x][y]:
                        licznik+=1
            if licznik*3>n1**2:
                return True
            
    return False