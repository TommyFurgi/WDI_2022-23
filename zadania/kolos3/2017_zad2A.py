'''Dane są dwie listy cykliczne powstałe przez zapętlenie listy jednokierunkowej posortowanej
rosnąco, dla każdej listy dany jest wskaźnik wskazujący przypadkowy element w takiej liście.
Proszę napisać funkcję, która dla dwóch list cyklicznych, usuwa z obu list elementy
występujące w obu listach. Do funkcji należy przekazać wskaźniki na dwie listy, funkcja
powinna zwrócić łączną liczbę usuniętych elementów.
'''
from Node import pokaz,stworz
class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

def zad(a,b):
    cnt=0
    while a.val<=a.next.val:
        a=a.next
    w1=a.next
    a.next=None

    while b.val<=b.next.val:
        b=b.next
    w2=b.next
    b.next=None

    g1=Node(None)
    g2=Node(None)
    g1.next=w1
    g2.next=w2
    prev1=g1
    prev2=g2
    while w1 is not None and w2 is not None:
        if w1.val==w2.val:
            cnt+=2
            print("usuwam",w1.val)
            prev1.next=w1.next
            prev2.next=w2.next

            tmp=w1.next
            w1.next=None
            w1=tmp

            tmp=w2.next
            w2.next=None
            w2=tmp
        elif w1.val>w2.val:
            w2=w2.next
            prev2=prev2.next
        else:
            w1=w1.next
            prev1=prev1.next
    while w1 is not None:
        w1=w1.next
        prev1=prev1.next

    while w2 is not None:
        w2=w2.next
        prev2=prev2.next
    
    prev1.next=g1.next
    prev2.next=g2.next
    g1.next=None
    g2.next=None
    return cnt
    
a=stworz([2,4,6,33,43,56,444])
b=stworz([2,3,4,5,6])

r=a
while r.next is not None:
    r=r.next
r.next=a

r=b
while r.next is not None:
    r=r.next
r.next=b

print(zad(a,b))