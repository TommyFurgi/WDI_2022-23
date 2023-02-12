class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    

def polacz(a,b):# b sorted
    wartownik=Node(0,b)
    prev=wartownik
    while a is not None:
        r=wartownik.next
        prev=wartownik
        while r is not None and a.val>r.val:
            r=r.next
            prev=prev.next
                    
        if r is None or a.val!=r.val:
            prev.next=a
            tmp=a.next
            a.next=r
            a=tmp
        else:
            a=a.next

    b=wartownik.next
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


g=Node(4,)
i=Node(7,g)
j=Node(2,i)
k=Node(8,j)

pokaz(zb)
pokaz(k)
print("========")
print(polacz(k,zb))
pokaz(zb)
pokaz(k)