'''Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego hetmana szachowego aby żaden hetman nie
zagrażał hetmanowi z sąsiedniego wiersza. Dodatkowo, suma wartości pól zajmowanych przez wszystkie figury była
równa zero. '''
def czy_mozna(t,a,b):
    for i in range(len(t)):
        if t[a][i]==1:
            return False
        if t[i][b]==1:
            return False

    for i in range(-len(t),len(t)):
        if 0<=a+i<len(t) and 0<=i+b<len(t):
            if t[a+i][b+i]==1:
                return False
        if 0<=a+i<len(t) and 0<=i-b<len(t):
            if t[a+i][b+i]==1:
                return False
    return True

def fun(t):
    tab=[[0 for _ in range(len(t))] for _ in range(len(t))]
    def rek(t,tab,pos=0,suma=0):
        if pos==len(t):
            if suma==0:
                return True
            return False
        
        for i in range(len(t)):
            if czy_mozna(tab,pos,i):
                tab[pos][i]=1
                if rek(t,tab,pos+1,suma+t[pos][i]):
                    return True
        
    return False