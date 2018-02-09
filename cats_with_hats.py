cats = {}

for i in range(1, 101):
    cats[i] = 0

for i in range(1, 101):
    for c in cats:
        if c % i == 0:
            if cats[c] == 0:
                cats[c] = 1
            else:
                cats[c] = 0

for c in cats:
    if cats[c] == 1:
        print('Cat #{} has a hat.'.format(c))
            
    
    
