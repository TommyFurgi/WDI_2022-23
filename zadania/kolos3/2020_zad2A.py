from Node import pokaz,stworz
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def zad(a):
    w=Node(None)
    w.next=a
    prev=w
    r=a
    najdl=0
    flag=False
    while r is not None:
        dl=0
        if r.next is not None and r.val==r.next.val:
            k=r.val
            tmp=prev
            while r is not None and r.val==k:
                dl+=1
                r=r.next
                tmp=tmp.next
            if dl==najdl:
                flag=False

            if dl>najdl:
                flag=True
                najdl=dl
                first=prev
                last=r
            prev=tmp
        else:
            r=r.next
            prev=prev.next

    if flag==True:
        r=first.next
        first.next=last
        while r is not None and r is not last:
            tmp=r.next
            r.next=None
            r=tmp
    r=w.next
    w.next=None
    return r

def zad2(a): # to samo ale inne rozw
    if a is None:
        return a
    g1=Node(None,a)
    g1.next=a
    prev=g1
    r=a
    najdl=0
    first=None
    while r is not None:
        if r.next is not None:
            tmp=prev
            q=r
            dl=0
            while q is not None and r.val==q.val:
                prev=prev.next
                dl+=1
                q=q.next
            if dl>najdl and dl>1:
                first=tmp
                last=q
                najdl=dl
            elif dl==najdl:
                first=None
                last=None
            r=q
        else:
            r=r.next
    if first is not None:
        first.next=last
    return g1.next

a = stworz([1, 3, 3, 3, 5, 11, 13, 13, 1, 2, 2, 2, 2])
pokaz(a)
a=zad2(a)
pokaz(a)

'''
def zad(a):
    if a is None:
        retur a
    g1=Node(None,a)
    prev=g1
    r=a
    najdl=0
    first=None
    while r is not None:
        if r.next is not None:
            tmp=prev
            q=r
            dl=0
            while q is not None and r.val==q.val:
                prev=prev.next
                dl+=1
                q=q.next
            if dl>najdl and dl>1:
                fist=tmp
                last=q
                najdl=dl
            elif dl==najd:
                first=None
                last=None
            r=q
        else:
            r=r.next
    if first is not None:
        first.next=last
    return g1.next
'''