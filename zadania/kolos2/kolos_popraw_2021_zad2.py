def czy_samogloska(x):
    if x=='a' or x=='e' or x=='y' or x=='o' or x=='u' or x=='i':
        return True
    return False

def cutting(s):
    def rek(s,pos=0,ile=0):
        if ile>1:
            return 0
        if pos==len(s):
            if ile==1:
                return 1
            return 0
        if czy_samogloska(s[pos]):
            ile+=1
        if ile==1:
            return rek(s,pos+1,ile) + rek(s,pos+1,0)
        else:
            return rek(s,pos+1,ile)
    
    return rek(s)

print(cutting("informatyka"))