from random import choice

def makePoem():
    nouns = ["fossil","horse","aardvark","judge","chef","mango","extrovert","gorilla"]
    verbs = ["kicks","jingles","bounces","slurps","meows","explodes","curdles"]
    adjectives = ["furry","balding","incredulous","fragrant","exuberant","glistening"]
    prepositions = ["against","after","into","beneath","upon","for","in","like","over","within"]
    adverbs = ["curiously","extravagantly","tantalizingly","furiously","sensuously"]
    vowels = ['a','e','i','o','u']

    noun_selection = []

    while len(noun_selection) < 3:
        new_noun = choice(nouns)
        if new_noun in noun_selection:
            continue
        else:
            noun_selection.append(new_noun)

    verb_selection = []

    while len(verb_selection) < 3:
        new_verb = choice(verbs)
        if new_verb in verb_selection:
            continue
        else:
            verb_selection.append(new_verb)

    adjective_selection = []

    while len(adjective_selection) < 3:
        new_adjective = choice(adjectives)
        if new_adjective in adjective_selection:
            continue
        else:
            adjective_selection.append(new_adjective)

    preposition_selection = []

    while len(preposition_selection) < 2:
        new_preposition = choice(prepositions)
        if new_preposition in preposition_selection:
            continue
        else:
            preposition_selection.append(new_preposition)

    adverb = choice(adverbs)

    if adjective_selection[0][0] in vowels:
        aan = 'An'
    else:
        aan = 'A'

    return """{0} {1} {2}

    {0} {1} {2} {3} {4} the {5} {6}
    {12}, the {2} {7}
    the {6} {10} {11} a {8} {9}""".format(aan,adjective_selection[0],noun_selection[0],verb_selection[0],\
                                         preposition_selection[0],adjective_selection[1],noun_selection[1],\
                                         verb_selection[1],adjective_selection[2],noun_selection[2],\
                                         verb_selection[2],preposition_selection[1],adverb)

print(makePoem())
                                                                
                                                        
                                                                    
