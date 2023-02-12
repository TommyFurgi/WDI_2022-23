from random import randint
def prob(n):
    year=[-1 for _ in range(365)]
    counter=0
    for i in range(100):
        for j in range(n):
            birthday=randint(0,364)
            if(year[birthday]==i):
                counter+=1
                break
            year[birthday]=i
    return counter/100
print(prob(35))