class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def warunek(liczba):
    jed=0
    dwoj=0
    while liczba>0:
        if liczba%3==1:
            jed+=1
        elif liczba%3==2:
            dwoj+=1
        liczba//=3
    if dwoj < jed:
        return False
    return True
    

def usun(zb):
    if zb is None:
        return

    flag=False    
    r=zb
    while r is not None:
        if warunek(r.val):
            if flag==False:
                zb=r
                flag=True
            else:
                zb.next=r
                zb=zb.next
        r=r.next
    zb.next=None

def pokaz(zb):
    r=zb
    while r is not None:
        print(r.val, end=",")
        r=r.next
    print()

d=Node(5)
c=Node(14,d)
b=Node(1,c)
a=Node(2,b)
zb=Node(2,a)

pokaz(zb)
usun(zb)
print("=======")
pokaz(zb)