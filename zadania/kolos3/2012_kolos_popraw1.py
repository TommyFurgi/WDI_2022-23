'''Mamy 2 uporządkowane listy jednokierunkowe. Napisz funkcję, która zwróci wskaźnik na różnicę
symetryczną z obu list (czyli taki XOR
'''

from Node import pokaz,stworz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def zad(a,b):
    g1=Node(None,a)
    g2=Node(None,b)

    prev1=g1
    prev2=g2
    w1=a
    w2=b

    while a is not None and b is not None:
        if a.val==b.val:
            prev1.next=a.next
            tmp=a.next
            a.next=None
            a=tmp
            b=b.next
            prev2=prev2.next
        elif a.val<b.val:
            a=a.next
            prev1=prev1.next
        else:
            tmp=b.next
            prev1.next=b
            prev1=prev1.next
            b.next=a
            prev2.next=tmp
            b=tmp
            prev2=prev2.next
    if a is None:
        prev1.next=b
 
    return g1.next

a=stworz([2,3,4,6,7,8])
b=stworz([3,5,7,9,11])
zb=zad(a,b)
pokaz(zb)