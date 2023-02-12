class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    

def zawieranie(a,b):
    flag1=True
    flag2=True
    p=a
    while a is not None:
        r=b
        while r is not None:
            if r.val==a.val:
                break
            r=r.next
        else:
            flag1=False
            break
        a=a.next

    if flag1==True:
        return True

    a=p
    while b is not None:
        r=a
        while r is not None:
            if r.val==b.val:
                break
            r=r.next
        else:
            flag2=False
            break
        b=b.next

    if flag2==True:
        return True
    return False

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


g=Node(11,)
i=Node(7,g)
j=Node(2,i)
k=Node(7,j)

pokaz(zb)
pokaz(k)
print("========")
print(zawieranie(k,zb))
