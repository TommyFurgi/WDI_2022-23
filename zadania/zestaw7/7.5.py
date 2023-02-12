class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val)
        r=r.next

def fun(a):
    pocz=[None for _ in range(10)]
    kon=[None for _ in range(10)]

    while a is not None:
        i=a.val%10
        r=a.next
        if pocz[i]==None:
            pocz[i]=a
            kon[i]=a
        else:
            a.next=pocz[i]
            pocz[i]=a
        a=r

    g=None
    for i in range(9,-1,-1):
        if kon[i] is not None:
            kon[i].next=g
            g=pocz[i]

    return g

a=Node(12)
b=Node(8)
c=Node(9)
d=Node(23)
e=Node(123)
f=Node(5)
g=Node(1)
h=Node(2)
i=Node(11)
    
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
g.next=h
h.next=i

pokaz(a)
a=fun(a)
print("================")
pokaz(a)