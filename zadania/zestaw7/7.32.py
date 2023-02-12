class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def roznica(a,b):
    p=Node(None,None)
    r=p
    while a is not None or b is not None:
        v=0
        if a is not None:
            v+=a.val
            a=a.next
        if b is not None:
            v-=b.val
            b=b.next
        new=Node(v,None)
        r.next=new
        r=r.next
    return p.next

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

def pokazw(zb):
    w=Node(None,zb)
    r = zb
    prev=w
    while r is not None:
        if r.next is None and r.val == 0:
            break
        print(r.val, end=",")
        
        r=r.next
        prev=prev.next
        
    print()

d=Node(16)
c=Node(5,d)
b=Node(5,c)
a=Node(3,b)
zb=Node(2,a)


f=Node(16)
g=Node(5,f)
i=Node(5,g)
j=Node(4,i)
k=Node(2,j)

pokaz(zb)
pokaz(k)
print("========")
p=roznica(zb,k)
pokazw(p)