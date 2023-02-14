class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def ile_poziomow(wsk):
    if wsk is None:
        return 0
    return 1+max(ile_poziomow(wsk.left),ile_poziomow(wsk.right))

def czy_jest_drzewemAVL(wsk,a=0,b=float('inf')):#zakladam że drzewo nie jest puste
    if wsk is None:
        return True
    if wsk.val<=a or wsk.val>=b or abs(ile_poziomow(wsk.left)-ile_poziomow(wsk.right))>=2:
        return False
    return czy_jest_drzewemAVL(wsk.left,a,wsk.val) and czy_jest_drzewemAVL(wsk.right,wsk.val,b)

a=Node(9)
b=Node(14)
c=Node(12,a,b)
d=Node(19)
e=Node(23,d)
f=Node(17,c,e)
g=Node(67)
h=Node(54,None,g)
i=Node(76)
j=Node(72,h,i)
k=Node(50,f,j)
print(czy_jest_drzewemAVL(k))