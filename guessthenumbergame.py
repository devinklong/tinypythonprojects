# Guess the Number Game 
import random 

def thenumber(x):
    randomnumber = random.randint(1, x)
    thenumber = 0 
    while thenumber != randomnumber:
        thenumber = int(input(f'Guess the number between 1 and {x}: '))
        if thenumber < randomnumber:
            print('Sorry, your guess was too low.')
        elif thenumber > randomnumber:
            print('Sorry, your guess was too high.')
        
    print(f'Yay! You got the number {randomnumber} correct! Good job.')

thenumber(100)

def computerguess(x):
    low = 1 
    high = x 
    feedback = ''
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #can also be high because they equal the same 
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()  
        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low == guess + 1  

    print(f"Yay, the computer got the number {guess} correctly!")

computerguess(10)






        


