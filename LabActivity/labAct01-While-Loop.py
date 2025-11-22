# Sum of Even Numbers

numToSum = int(input('Enter a number: '))
sumEven = 0
current = 2

while current <= numToSum:
    for num01 in range(current, numToSum + 1, 2):  
        print(f'{sumEven} + {num01}')
        sumEven += num01
    break

print(f'The sum of all even numbers is: {sumEven}')

print('')
# Factor Finder

numToFactor = int(input('Enter a number to find the factors: '))

while True:
    for num02 in range(1, numToFactor + 1):
        if numToFactor % num02 == 0:
            print(num02)
    break

print('')
# Simple ATM Menu

print('Press 1 to Deposit')
print('Press 2 to Withdraw')
print('Press 3 to Check Balance')
print('Press 4 to Exit')

menu = ''
balance = 0

while menu != '4':
    menu = input('Input your chosen number: ')

    if menu == '1':
        deposit = int(input('Enter the desired deposit amount: '))
        balance += deposit
        print(f'Your balance is: ${balance}')
    elif menu == '2':
        withdraw = int(input('Enter the desired withdraw amount: '))
        balance -= withdraw
        print(f'Your balance is: ${balance}')
    elif menu == '3':
        print(f'Your balance is: ${balance}')
    elif menu == '4':
        break
    else:
        print('Invalid input. Please try again.')