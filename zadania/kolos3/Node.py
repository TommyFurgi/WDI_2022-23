class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def pokaz(a):
    while a is not None:
        print(a.val, end=",")
        a=a.next
    print()
    
def stworz(tab):
    g=Node(Node)
    p=g
    for i in tab:   
        p.next=Node(i)
        p=p.next
    
    return g.next
