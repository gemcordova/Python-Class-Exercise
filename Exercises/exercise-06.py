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