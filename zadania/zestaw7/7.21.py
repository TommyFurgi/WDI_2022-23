class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def usun(zb): # z wartownikiem
    if zb.next is None:
        return 

    pocz=zb
    pocz2=zb
    dl=1
    najdl=0
    r=zb.next
    p=r.next
    kon=None
    while p is not None:
        if r.val<p.val:
            dl+=1
        else:
            if dl>najdl:
                pocz2=pocz
                najdl=dl
                kon=p
            pocz=r
            dl=1
        p=p.next
        r=r.next
    tmp=pocz2.next 
    pocz2.next=kon
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
zb=Node(0,a)#wartownik

pokaz(zb)
usun(zb)
print("=======")
pokaz(zb)