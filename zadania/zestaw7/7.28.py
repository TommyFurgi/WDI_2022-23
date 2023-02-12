class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def usun_wystepujace(a,b):#b sorted
    w1=Node(0,a)
    w2=Node(0,b)
    prev1=w1
    prev2=w2
    ile=0
    flag=False
    while a is not None:
        b=w2.next
        prev2=w2
        while b is not None and a.val>=b.val:
            if a.val==b.val:
                flag=True
                prev1.next=a.next
                prev2.next=b.next
                print("usuwam",a.val)
                ile+=2
            prev2=prev2.next
            b=b.next
        if flag==False:
            prev1=prev1.next
        flag=False
        a=a.next

    a=w1.next
    b=w2.next
    return ile


def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()


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
