from Node import stworz,pokaz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def zad(a,b):
    if a is None or b is None:
        return 0
    
    cnt=0
    g1=Node(None,a)
    g2=Node(None,b)
    prev1=g1
    prev2=g2
    
    while a is not None and b is not None:
        if a.val==b.val:
            print("usuwam",a.val)
            cnt+=2
            tmp=a.next
            prev1.next=a.next
            a.next=None
            a=tmp

            tmp=b.next
            prev2.next=tmp
            b.next=None
            b=tmp

        elif a.val>b.val:
            prev2=prev2.next
            b=b.next
        else:
            a=a.next
            prev1=prev1.next
    
    tmp=g1.next
    g1.next=None
    a=tmp

    tmp=g2.next
    g2.next=None
    b=tmp

    return cnt

a=stworz([1,2,3,4,5,7,8])
b=stworz([0,2,4,6,8,10])
pokaz(a)
pokaz(b)
print("===========")
print(zad(a,b))
pokaz(a)
pokaz(b)