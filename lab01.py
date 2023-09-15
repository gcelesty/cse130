# 1. Name: 
#    Celeste George
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    Write a program in python to display a message on the screen, prompt user for information,
#    make a decision, store data in a list, and loop.
# 4. What was the hardest part? Be as specific as possible.
#    The most difficult things in this assignment would be storing the data. 
#    Having to set up an array for the data to be store and then having to
#    store the users answers themselves was a bit tricky. However, once I figured
#    it out everything else fell into place.
# 5. How long did it take for you to complete the assignment?
#    The assignment took me roughly 3 hours since I had to do additional reading to understand
#    storing data into an array. I also watched a couple tutorials on YouTube that demonstrated
#    how to store what the user response is into the array itself.

import random

# ask user
print('\nThis is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.')
value_max = int(input('\nPick a positive integer: '))

# generate random number
value_random = random.randint(1, value_max)

print(f'Guess a number between 1 and {value_max}')
list = []
count = 0

while True:
    guess = int(input('> '))
    list.append(guess)
    count += 1

    if guess > value_random:
        print('     Too high!')
    elif guess < value_random:
        print('     Too low!')
    else:
        print(f'You were able to find the number in {count} guesses.')
        break

print(f'The numbers you guessed were: {list}')