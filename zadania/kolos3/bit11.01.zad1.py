from Node import pokaz,stworz

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def fun(a,b):
    g1=Node(None,a)
    prev1=g1
    r=a
    cnt=0
    while r is not None:
        q=b
        while q is not None:
            if q==r:
                while q is not None:
                    cnt+=1
                    prev1.next=Node(q.val)
                    prev1=prev1.next
                    q=q.next
                
                tmp=g1.next
                g1.next=None
                a=tmp
                return cnt


            q=q.next
        r=r.next
        prev1=prev1.next

e=Node(3)
d=Node(2,e)
c=Node(3,d)
b=Node(11,c)
a=Node(5,b)

y=Node(17,c)
x=Node(7,y)
zb=Node(13,x)


pokaz(a)
pokaz(zb)
print(fun(a,zb))