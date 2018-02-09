from capitals import capitals_dict
import random

capitals_list = list(capitals_dict.keys())

while True:
    state = random.choice(capitals_list)
    capital = capitals_dict[state]

    guess = input('What is the capital of {}?\n'.format(state))

    if capital.lower() == guess.lower():
        print("Correct!")
        break
    elif guess.lower() == 'exit':
        print("Goodbye :(")
        break

        
