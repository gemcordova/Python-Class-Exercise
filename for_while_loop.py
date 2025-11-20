# Exercise 1: Multiplication Table Generator

num01 = int(input('Enter a number: '))

for product in range(1, 11):
    print(f'{num01} x {product} = {num01 * product}')

# Exercise 2: Sum of Even Numbers (1 to N)

num02 = int(input('Enter a number: '))
even_add = 0

for even_num in range(1, num02 + 1):
    if even_num % 2 == 0:
        even_add += even_num

print(f'The sum of even numbers from 1 to {num02} is: {even_add}')

# Exercise 3: Star Pattern Pyramid

row = int(input('Enter number of row: '))

for star in range(1, row + 1):
    print('*' * star)

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

# Exercise 5: Running Total Calculator

total = 0
num = 1

while num != 0:
    num = int(input('Enter a number (0 to exit): '))
    total += num

print(f'Your total is: {total}')

# Exercise 6: Login Attempt Limiter

correct_pass = 'iLovePizza'
attempt = 0

while attempt < 3:
    password = input('Enter your password: ')

    if password == correct_pass:
        print('Login Successful!')
        break
    else:
        print('Incorrect Password')
        attempt += 1

if attempt == 3:
    print('Account Locked')
