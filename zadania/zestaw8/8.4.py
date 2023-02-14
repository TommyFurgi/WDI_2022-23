class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def ile_poziomow(wsk):
    if wsk is None:
        return 0
    return 1+max(ile_poziomow(wsk.left),ile_poziomow(wsk.right))

a=Node(10)
b=Node(5,a)
c=Node(2)
e=Node(8)
d=Node(7,c,e)
f=Node(3,b)
g=Node(1,d,f)
print(ile_poziomow(g))