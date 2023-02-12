'''Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
powinna zwrócić łączną liczbę usuniętych elementów.
'''

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

def usun_wystepujace(a,b):#b sorted
    g1=Node(None,a)
    g2=Node(None,b)
    prev1=g1
    w1=a
    cnt=0
    while w1 is not None:
        prev2=g2
        w2=g2.next
        while w2 is not None and w2.val<=w1.val:
            if w2.val==w1.val:
                cnt+=1
                tmp=w2.next
                prev2.next=tmp
                w2.next=None

                tmp=w1.next
                prev1.next=tmp
                w1.next=None
                w1=tmp
                break

            w2=w2.next
            prev2=prev2.next
        else:
            prev1=w1
            w1=w1.next
            
    tmp=g1.next
    g1.next=None
    a=tmp

    tmp=g2.next
    g2.next=None
    b=tmp
    return cnt

d=Node(5)
c=Node(14,d)
b=Node(5,c)
a=Node(2,b)
zb=Node(3,a)

f=Node(15)
g=Node(14,f)
i=Node(5,g)
j=Node(3,i)
k=Node(2,j)

pokaz(zb)
pokaz(k)
print("========")
print(usun_wystepujace(zb,k))
