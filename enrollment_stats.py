universities =	[
                 ['California Institute	of Technology',	2175, 37704],
                 ['Harvard', 19627, 39849],
                 ['Massachusetts Institute of Technology', 10566, 40732],
                 ['Princeton', 7802, 37000],
                 ['Rice', 5879, 35551],
                 ['Stanford', 19535, 40569],
                 ['Yale', 11701, 40500]
                 ]


def enrollment_stats(lol):
    students = []
    tuition = []
    for l in lol:
        students.append(l[1])
        tuition.append(l[2])
    return students, tuition

def total(l):
    tot = 0
    for i in l:
        tot += i
    return tot

def mean(l):
    return float(total(l)) / float(len(l))

def median(l):
    l.sort()    
    size = len(l)
       
    if size % 2 == 0:
        midpoint = int(size / 2)
        return (l[midpoint - 1] + l[midpoint]) / 2.0
    else:
        midpoint = int((size + 1) / 2)
        return l[midpoint - 1]


students, tuition = enrollment_stats(universities)

print('Total students: {}'.format(total(students)))
print('Total tuition: ${}'.format(total(tuition)))
print()
print('Student mean: {}'.format(mean(students)))
print('Student median: {}'.format(median(students)))
print()
print('Tuition mean: ${}'.format(mean(tuition)))
print('Tuition median: ${}'.format(median(tuition)))
        

    

    
        
