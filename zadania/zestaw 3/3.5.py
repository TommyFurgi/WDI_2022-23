def umiesc_w_liscie(tablica, wpisana):
    for i in range(9):
        if(tablica[i]>=wpisana):
            temp=tablica[i]
            tablica[i]=wpisana
            p=i

            while p<9 and temp!=0:
                temp,tablica[p+1]=tablica[p+1],temp
                p+=1
            return
                
        elif tablica[i]==0:
            tablica[i]=wpisana
            return 
    return

liczba=input()
tablica=[0]*10
wpisana=1
for i in liczba:
    wpisana=int(i)
    if wpisana==0:
        break
    else:
        umiesc_w_liscie(tablica,wpisana)

print(tablica)
print(tablica[9])