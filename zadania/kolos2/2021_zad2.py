'''
Zadanie 4 (5 pkt)
W tablicy o rozmiarze N na N wypełnionej liczbami naturalnymi umieszczono dokładnie jeden fragment ciągu Fibonacciego o długości co najmniej 3 elementów. Cały fragment leży w jednym z wierszy
lub kolumn w kierunku rosnącym lub malejącym. Prosze napisać funkcję, która dla zadanej tablicy
odszuka ten fragment i zwróci jego wartość.
'''
def ciag(n):
    a,b=1,1
    while b<=n:
        if n==b:
            return True
        a,b=b,a+b
    return False

def fun(T):
    a,b,c=0,0,0
    for i in range(len(T)):
        for j in range(len(T)):
            if ciag(T[i][j]):
                a=T[i][j]
                if i+2<len(T):
                    if ciag(T[i+1][j]):
                        b=T[i+1][j]
                        if ciag(T[i+2][j]):
                            c=T[i+2][j]
                            if a+b==c or c+b==a:
                                return True

                if j+2<len(T):
                    if ciag(T[i][j+1]): 
                        b=b=T[i][j+1]
                        if ciag(T[i][j+2]):
                            c=T[i][j+2]
                            if a+b==c or c+b==a:
                                return True
    return False

T=[[13,5,5],
    [4,6,8],
    [5,7,13]]
print(fun(T))