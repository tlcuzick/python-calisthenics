import os
import csv

path = 'C:/Users/TLC/Desktop/Python Web Development/Part 1/book1-exercises-master/chp09/practice_files'

high_scores = {}

with open(os.path.join(path, 'scores.csv'), 'r') as scores:
    scores_reader = csv.reader(scores)
    for row in scores_reader:
        name = row[0]
        score = int(row[1])
        if name in high_scores:
            if score > int(high_scores[name]):
                high_scores[name] = score
        else:
            high_scores[name] = score
            
for s in sorted(high_scores):
    print('{} {}'.format(s, high_scores[s]))
        
