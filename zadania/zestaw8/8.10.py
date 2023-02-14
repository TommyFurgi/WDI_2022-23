class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def czy_nalezy(wsk,n):
    if wsk is None:
        return False
    if wsk.val==n:
        return True
    elif n>wsk.val:
        return czy_nalezy(wsk.right,n)
    else:
        return czy_nalezy(wsk.left,n)

a=Node(13)
b=Node(14,a)
c=Node(10,None,b)
d=Node(4)
e=Node(7)
f=Node(6,d,e)
g=Node(1)
h=Node(3,g,f)
i=Node(8,h,c)
print(czy_nalezy(i,11))
