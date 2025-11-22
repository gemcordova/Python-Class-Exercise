# Exercise 1: Multiplication Table Generator

num01 = int(input('Enter a number: '))

for product in range(1, 11):
    print(f'{num01} x {product} = {num01 * product}')