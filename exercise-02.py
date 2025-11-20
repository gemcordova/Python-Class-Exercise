# Exercise 2: Sum of Even Numbers (1 to N)

num02 = int(input('Enter a number: '))
even_add = 0

for even_num in range(1, num02 + 1):
    if even_num % 2 == 0:
        even_add += even_num

print(f'The sum of even numbers from 1 to {num02} is: {even_add}')
