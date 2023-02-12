class Node:
    def __init__(self,val1,val2,next=None):
        self.val1=val1
        self.val2=val2
        self.next=next
    
def scal(a,b,c,d):
    if b>=c and a>=d:
        return min(a,c),max(b,d)
    return None

def przedzialy(p): 
    res=p
    while p is not None:
        q=p.next
        prev=p
        while q is not None:
            test=scal(p.val1,p.val2,q.val1,q.val2)
            if test is not None:
                p.val1,p.val2=test
                prev.next=q.next
            else:
                prev=q
            q=q.next
        p=p.next
    return res

def pokaz(zb):
    r=zb
    while r is not None:
        print("[",r.val1, r.val2,"]", end=", ")
        r=r.next
    print()

e=Node(13,17)
d=Node(5,6,e)
c=Node(8,12,d)
b=Node(7,11,c)
a=Node(2,5,b)
zb=Node(15,19,a)


pokaz(zb)
print("========")
a=print(przedzialy(zb))
pokaz(a)