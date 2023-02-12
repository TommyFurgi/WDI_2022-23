'''
Dane są dwa jednokierunkowe łańcuchy odsyłaczowe (listy) zbudowane z elementów:
struct node { int w; node* next; };
Każdy łańcuch zawiera niepowtarzające się liczby naturalne. W obu łańcuchach liczby są posortowane rosnąco.
Proszę napisać funkcję usuwającą z każdego łańcucha liczby nie występujące w drugim. Do funkcji należy przekazać
wskazania na oba łańcuchy, funkcja powinna zwrócić łączną liczbę usuniętych elementów.
'''
from Node import pokaz,stworz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=Node

def zad(a,b):
    g1=Node(None,a)
    g2=Node(None,b)
    prev1=g1
    prev2=g2
    w1=a
    w2=b
    cnt=0
    while w1 is not None or w2 is not None:
        if w1 is None:
            cnt+=1
            tmp=w2.next
            w2.next=None
            prev2.next=tmp
            w2=tmp

        elif w2 is None:
            cnt+=1
            tmp=w1.next
            w1.next=None
            prev1.next=tmp
            w1=tmp

        elif w1.val==w2.val:
            w1=w1.next
            w2=w2.next
            prev1=prev1.next
            prev2=prev2.next

        elif w1.val>w2.val:
            cnt+=1
            tmp=w2.next
            w2.next=None
            prev2.next=tmp
            w2=tmp
        else:
            cnt+=1
            tmp=w1.next
            w1.next=None
            prev1.next=tmp
            w1=tmp
    return cnt


a=stworz([2,3,5,7,8])
b=stworz([1,6,7,8])
print(zad(a,b))

