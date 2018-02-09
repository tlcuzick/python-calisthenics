from random import random

gwa = 0
gwb = 0

for i in range(1, 10001):
    rwa = 0
    rwb = 0
    
    randval = random()

    if randval < 0.87:
        rwa += 1
    elif randval > 0.87:
        rwb += 1

    randval = random()

    if randval < 0.65:
        rwa += 1
    elif randval > 0.65:
        rwb += 1

    randval = random()

    if randval < 0.17:
        rwa += 1
    elif randval > 0.17:
        rwb += 1

    if rwa > rwb:
        gwa += 1
    elif rwb > rwa:
        gwb += 1

cap = float(gwa) / (gwa + gwb)
cbp = float(gwb) / (gwa + gwb)

print('There is a {}% chance candidate A will win.'.format(round(cap * 100, 2)))
print('There is a {}% chance candidate B will win.'.format(round(cbp * 100, 2)))

        
