class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    

def iteracyjnie(a,b):
    wartownik=Node(0,a)
    prev=wartownik
    while b is not None:
        r=a
        prev=wartownik
        while r is not None and r.val < b.val:
            r=r.next
            prev=prev.next

        if r is None or r.val != b.val:
            tmp=b.next
            b.next=r
            prev.next=b
            b=tmp
        else:
            b=b.next

    a=wartownik.next
    wartownik.next=None


def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

d=Node(11)
c=Node(7,d)
b=Node(5,c)
a=Node(3,b)
zb=Node(2,a)


g=Node(8,)
i=Node(7,g)
j=Node(4,i)
k=Node(2,j)

pokaz(zb)
pokaz(k)
print("========")
iteracyjnie(zb,k)
pokaz(zb)
