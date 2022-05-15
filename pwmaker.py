import random 

print("This is a password making Python program")

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+-=;:,./?<>'

number = input('Amount of passwords to create: ')
number = int(number)

length = input('Amount of charactters in password: ')
length= int(length)

print('\nThese are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
