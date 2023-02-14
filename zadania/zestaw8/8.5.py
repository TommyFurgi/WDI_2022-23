class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def ile_lisci(wsk):
    if wsk is None:
        return 0
    elif wsk.right is None and wsk.left is None:
        return 1
    else:
        return ile_lisci(wsk.right)+ile_lisci(wsk.left)

a=Node(10)
b=Node(5,a)
c=Node(2)
e=Node(8)
d=Node(7,c,e)
f=Node(3,b)
g=Node(1,d,f)
print(ile_lisci(g))