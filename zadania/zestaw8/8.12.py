class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def czy_jest_drzewemBTS(wsk,a=0,b=float('inf')):#zakladam że drzewo nie jest puste
    if wsk is None:
        return True
    if wsk.val<=a or wsk.val>=b:
        return False
    return czy_jest_drzewemBTS(wsk.left,a,wsk.val) and czy_jest_drzewemBTS(wsk.right,wsk.val,b)

a=Node(13)
b=Node(14,a)
c=Node(10,None,b)
d=Node(4)
e=Node(7)
f=Node(6,d,e)
g=Node(1)
h=Node(3,g,f)
i=Node(8,h,c)
print(czy_jest_drzewemBTS(i))