class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def liczba(r,a=0,pos=0):
    if r is None:
        return a
    
    return liczba(r.next,r.val+(a * 10),pos+1)

def sumuj_listy(a,b):
    l1=liczba(a)
    l2=liczba(b)
    s=l1+l2

    if s==0:
        new=Node(0,None)
        return new

    prev=None
    while s!=0:
        r=Node(s%10,None)
        s//=10
        if prev is not None:
            r.next=prev
        prev=r

    return prev

def pokaz(r):
    while r is not None:
        print(r.val, end="")
        r=r.next
    print()
    
d=Node(8,None)
c=Node(5,d)
b=Node(3,c)


v=Node(9,None)
x=Node(5,v)
y=Node(2,x)


print(liczba(b))
print(liczba(y))
zb=sumuj_listy(b,y)
pokaz(zb)