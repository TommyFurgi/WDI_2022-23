'''1. Dana jest tablica wypełniona liczbami naturalnymi:
const int N=1000; int t[N][N];
Proszę napisać funkcję, która poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą
większą od 1, którego iloczyn 4 pól narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość
k. Funkcja powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz,
kolumna) środka kwadratu
'''
def fun(T,k):
    n=len(T)
    for dl in range(3,n): #min 2x2
        if dl%2==1:
            for i in range(n-dl+1):
                for j in range(n-dl+1):
                    s1=T[i][j]+T[i+dl-1][j]+T[i+dl-1][j+dl-1]+T[i][j+dl-1]
                    if s1==k:
                        d=dl//2
                        return True, i+d, j+d

    return False