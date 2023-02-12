from Node import stworz,pokaz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def zad(a,b,c):
    if a is None or b is None or c is None:
        return 0
    
    cnt=0
    g1=Node(None,a)
    g2=Node(None,b)
    g3=Node(None,c)
    prev1=g1
    prev2=g2
    prev3=g3
    
    while a is not None and b is not None and c is not None:
        if a.val==b.val and a.val==c.val:
            print("usuwam",a.val)
            cnt+=3
            tmp=a.next
            prev1.next=a.next
            a.next=None
            a=tmp

            tmp=b.next
            prev2.next=tmp
            b.next=None
            b=tmp

            tmp=c.next
            prev3.next=tmp
            c.next=None
            c=tmp

        else:
            k=min(a.val,b.val,c.val)
            if k==a.val:
                a=a.next
                prev1=prev1.next
            elif k==b.val:
                b=b.next
                prev2=prev2.next
            else:
                c=c.next
                prev3=prev3.next
    
    tmp=g1.next
    g1.next=None
    a=tmp

    tmp=g2.next
    g2.next=None
    b=tmp

    tmp=g3.next
    g3.next=None
    c=tmp

    return cnt

a=stworz([1,2,3,4,5,7,8])
b=stworz([0,2,4,6,8,10])
c=stworz([1,2,3,4,5,6])
pokaz(a)
pokaz(b)
pokaz(c)
print("===========")
print(zad(a,b,c))
pokaz(a)
pokaz(b)
pokaz(c)