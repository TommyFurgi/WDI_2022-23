def czy_samogloska(n):
    if n=="a" or n=='e'or n=='o' or n=='i' or n=='u' or n=='y':
        return True
    return False

def zad(napis,pos=0,ile=0,ciecia=0):
    if pos==len(napis):
        if ile>0 and ciecia!=0:
            return 1
        return 0
    litera=napis[pos]
    if czy_samogloska(litera):
        ile+=1

    if ile>=1:
        return zad(napis,pos+1,ile,ciecia) + zad(napis,pos+1,0,ciecia+1)
    else:
       return zad(napis,pos+1,ile,ciecia)

print(zad("ocena"))
    