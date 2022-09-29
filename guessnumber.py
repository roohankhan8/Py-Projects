import random

num = random.randint(0, 20)
guess = int(input('Guess The Number Between 0 to 10: '))
guesses = 0

while guess!=num:
    if guess<num:
        print('Higher')
    elif guess>num:
        print('Lower')
    guess = int(input('Guess The Number Between 0 to 10: '))
    guesses+=1
else:
    print('Perfect')
    print('Number Of Guesses: ' + str(guesses))
