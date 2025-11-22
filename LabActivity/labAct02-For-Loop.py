# 1. Print 1 to 20

givenNumber = 20
for num01 in range(1, givenNumber + 1):
    print(num01)

print('')
# 2. Even Numbers Only

evenNumber = 40
for num02 in range(2, evenNumber + 1):
    if num02 % 2 == 0:
        print(num02)

print('')
# 3. Sum of First 10 Numbers

sumOfTen = 10
total = 0
for num03 in range(1, sumOfTen + 1):
    print(total)
    total += num03

print('')
# 4. Print Characters in Words

givenWord = input('Enter a word: ')
len(givenWord)
for word in givenWord:
    print(word)

# 5. Multiplication Table (1 to 10)

productOfNum = int(input('Enter a number: '))
for num05 in range(1, 11):
    print(f'{productOfNum} x {num05} = {productOfNum * num05}')

print('')

# ======================================================================
# Intermediate For Loops
# 1. Factorial Calculator

factorialOfNum = int(input('Enter a number: '))
result = 1
for numA in range(1, factorialOfNum + 1):
    result *= numA
print(f"Factorial of {factorialOfNum} is {result}")

print('')
# 2. Count vowels on a String
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")

print('')
# 3. Reverse a Word
word = input("Enter a word: ")
reversedWord = word[::-1] 
print(f"Reversed word: {reversedWord}")

print('')
# 4. Squares of Numbers
squaredNum = int(input('Enter a number: '))

for numD in range(1, squaredNum + 1):
    print(f"{numD} squared = {numD**2}")

print('')
# 5. Pattern Printing
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

print('')
# 6. Prime Number Checker
numB = int(input("Enter a number: "))

if numB < 2:
    print(f"{numB} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(numB**0.5) + 1):
        if numB % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{numB} is a prime number.")
    else:
        print(f"{numB} is not a prime number.")

print('')
# 7. Sum of Digits
numC = int(input("Enter a number: "))
sumDigits = 0
numD = numC

while numD > 0:
    sumDigits += numD % 10
    numD //= 10

print(f"Sum of digits of {numC} is {sumDigits}")