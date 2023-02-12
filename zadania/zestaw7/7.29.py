class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def usun_niewystepujace(a,b):
    w1=Node(0,a)
    w2=Node(0,b)
    prev1=w1
    prev2=w2
    ile=0
    while a is not None and b is not None:
        if a.val==b.val:
            print(a.val)
            prev1.next=a.next
            prev2.next=b.next
            tmp1=a.next
            tmp2=b.next
            a.next=None
            b.next=None
            a=tmp1
            b=tmp2
            ile+=2
        elif a.val>b.val:
            b=b.next
            prev2=prev2.next
        elif a.val<b.val:
            a=a.next
            prev1=prev1.next
    
    a=w1.next
    b=w2.next
    w1.next=None
    w2.next=None
    return ile


def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()


d=Node(16)
c=Node(14,d)
b=Node(5,c)
a=Node(3,b)
zb=Node(2,a)

f=Node(15)
g=Node(14,f)
i=Node(5,g)
j=Node(4,i)
k=Node(2,j)

pokaz(zb)
pokaz(k)
print("========")
print(usun_niewystepujace(zb,k))
