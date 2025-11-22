# Exercise 5: Running Total Calculator

total = 0
num = 1

while num != 0:
    num = int(input('Enter a number (0 to exit): '))
    total += num

print(f'Your total is: {total}')
