class Node:
    def __init__(self,inx,val,next=None):
        self.inx=inx
        self.val=val
        self.next=next

def jaka_wartosc(inx,zb):
    r=zb
    while r is not None and inx>=r.inx:
        if inx==r.inx:
            return r.val
        r=r.next
    return 0 
    
a = Node(0,23)
b = Node(39,42)
c = Node(55,23)

a.next=b
b.next=c

print(jaka_wartosc(0,a))
print(jaka_wartosc(23,a))
print(jaka_wartosc(39,a))
print(jaka_wartosc(55,a))