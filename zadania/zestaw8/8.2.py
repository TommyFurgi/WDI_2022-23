class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def czy_nalezy(wsk,k):
    if wsk is None:
        return False
    elif wsk.val==k:
        return True
    else:
        return czy_nalezy(wsk.left,k) or czy_nalezy(wsk.right,k)

a=Node(10)
b=Node(5,a)
c=Node(2)
e=Node(8)
d=Node(7,c,e)
f=Node(3,b)
g=Node(1,d,f)
print(czy_nalezy(g,11))