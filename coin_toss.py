from random import randint

flips = 0
trials = 10000

for i in range(1, trials + 1):
    heads = 0
    tails = 0
    
    while heads == 0:
        flips += 1
        
        if randint(0,1) == 1:
            heads = 1
        elif tails == 0:
            tails = 1

    while tails == 0:
        flips += 1
        
        if randint(0,1) == 0:
            tails = 1

print(flips / trials)


