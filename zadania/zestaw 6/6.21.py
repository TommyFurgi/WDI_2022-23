def fun1(T,zadana):
    tab=[[0 for _ in range(len(T))] for _ in range(len(T))]
    def fun(T,zadana,w=0,suma=0):
        if w==len(T):
            if suma==zadana:
                return True
            else:
                return False

        for i in range(len(T)):
            if czy_mozna(tab,i):
                tab[w][i]=1
                if fun(T,zadana,w+1,suma+T[w][i]):
                    return True
                else:
                    tab[w][i]=0

        return False
    return fun(T,zadana)


def czy_mozna(tab,k):
    for i in range(len(tab)):
        if tab[i][k]==1:
            return False
    return True

T=[[3,4,5],
    [56,43,78],
    [9,45,3]]

print(fun1(T,49))