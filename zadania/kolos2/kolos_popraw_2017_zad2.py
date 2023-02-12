'''Dana jest tablica booli int t[N][N] reprezentująca szachownicę. Pole szachownicy ma
wartość true, jeżeli stoi na nim figura, a false, jeśli jest ono puste. Proszę napisać
funkcję która sprawdza czy istnieje droga skoczka przemieszczającego się z wiersza
0 do wiersza N-1. Skoczek może poruszać się tylko po polach pustych. Skoczek w
każdym ruchu powinien przybliżać się do N-1 wiersza. Funkcja ma zwrócić
najmniejszą możliwą liczbę ruchów. Skoczek może zacząć poruszać się z dowolnego
pustego pola z wiersza 0. N z zakresu 4...20.
'''

def zad(t):
    def rek(t,x,y,ruchy=0):
        if x==len(t) or y<0 or y>=len(t) or t[x][y]==True:
            return float('inf')
        if x==len(t)-1:
            return ruchy
        
        return min(rek(t,x+1,y+2,ruchy+1),rek(t,x+1,y-2,ruchy+1),rek(t,x+2,y+1,ruchy+1),rek(t,x+2,y-1,ruchy+1))

    ans=float('inf')
    for i in range(len(t)):
        ans=min(rek(t,i,0),ans)
    
    return ans

    