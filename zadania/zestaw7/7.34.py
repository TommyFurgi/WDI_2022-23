from Node import Node,stworz

def pokaz(zb):
    r=zb
    while True:
        print(r.val, end=", ")
        r=r.next
        if r is zb:
            break
    print()

def usun(zb,value):
    r=zb
    guard=Node(None,a)
    prev=guard
    while True:
        if r.val==value:
            prev.next=r.next
        else:
            prev=prev.next
        r=r.next
        if r.next is zb:
            r.next=guard.next
            return guard.next



def usun_z_listy(zb,k): # problem z usunieciem pierwszego elementu
    a=zb
    flag=False
    while True:
        counter=0
        r=a
        while True:
            if r.val==a.val:
                counter+=1
            r=r.next
            if r is a:
                break
        if counter==k:
            print("usun",a.val)
            a=usun(a,a.val)

            flag=True
        else:
            a=a.next
        if a is zb:
            break
    
    return flag



a=stworz([10,2,2,0,1,23,45,66,8,5,3,43,34,22,4444])
r=a
while r.next is not None:
    r=r.next
r.next=a

pokaz(a)
print(usun_z_listy(a,2))
pokaz(a)