# Exercise 4: Number Guessing Game

mystery_num = 69
guess = 0

while guess != mystery_num:
    guess = int(input('Enter your guess (1-100): '))

    if guess > mystery_num:
        print('Too High! Try Again')
    elif guess < mystery_num:
        print('Too Low! Try Again')
    else:
        print('Correct!')
