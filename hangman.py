# Hangman Python Game 
import random 
from hangmanwords import words
import string

def get_the_word(words): 
    word = random.choice(words) #randomly chooses a word from the hangmanwords list 
    while '-' in word or ' ' in word: 
        word = random.choice(words)

    return word.upper()

def hangman(): 
    word = get_the_word(words)
    word_letters = set(word) # letters in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letters the user has already guessed 

    lives = 6 

    # getting the user input 
    while len(word_letters) > 0 and lives > 0:
        # letters used 
        # ' '.join(['a', 'b', 'cd']) --> a b cd
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Put the letter you would like to guess here: ").upper()
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else: 
                lives = lives - 1 # takes a life away if letter isn't in the word
                print('The letter', user_letter, 'is not in the word')

    
        elif user_letter in used_letters:
            print("You have already used this letter, please try another non-used letter.")
    
        else:
            print("Invalid letter. Please try again.")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0: 
        print("Sorry, you're dead. The word was", word)
    print('You guessed the word', word, 'correctly!')

get_the_word(words)
hangman()