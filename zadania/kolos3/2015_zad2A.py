''' Dane są dwa jednokierunkowe łańcuchy odsyłaczowe (listy) zbudowane z elementów:
struct node { int w; node* next; };
Każdy łańcuch zawieraj niepowtarzające się liczby naturalne. W pierwszym łańcuchu liczby są
posortowane rosnąco, a w drugim nie. Proszę napisać funkcję usuwającą z obu łańcuchów liczby
występujące w obu łańcuchach. Do funkcji należy przekazać wskazania na oba łańcuchy, funkcja
powinna zwrócić łączną liczbę usuniętych elementów.
'''
from Node import pokaz,stworz
class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

def zad(a,b):#a sordted
    g1=Node(Node)
    g2=Node(Node)
    g1.next=a
    g2.next=b

    prev2=g2
    r=b
    cnt=0
    while r is not None:
        q=g1.next
        prev1=g1
        while q is not None and q.val<=r.val:
            if q.val==r.val:
                cnt+=2
                tmp=q.next
                prev1.next=tmp
                q.next=None

                tmp=r.next
                prev2.next=tmp
                r.next=None
                r=tmp
                break
            q=q.next
            prev1=prev1.next
        else:
            r=r.next
            prev2=prev2.next
    
    return cnt

    
a=stworz([2,4,6,33,43,56,444])
b=stworz([32,3,4,22,6])

print(zad(a,b))
pokaz(b)