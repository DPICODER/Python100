import random 

# importing os for cleaning the terminal for better experiance
import os

# imported the words from another python file
from Hangman_words import words

# importing logo and Hangman ascii from another file
from Hangman_ASCII import stages, logo

# generating a random word for user to guess
w_generated = random.choice(words)

print(logo)

# getting length of word generated
no_of_w = len(w_generated)

# creating a empty list for diplaying the word later
display = []

# adding _ , _ , as a placeholder and hint of word size
for letter in range(no_of_w):
    display += "_"


# print(w_generated)

print(display)

# no of lives declared
lives = 6
end_state = False


# Continious loop till game end_state not true
while not end_state:
    user_input = input("Enter a word as a Guess :").lower()
    
    os.system('cls')

    # if user input is in generated word add to display list
    for w in range(no_of_w):
        letter = w_generated[w]
        if user_input == letter:
            display[w] = user_input

    # message if same letter is entered multiple times
    if user_input in display:
        print(f"You have alread enterd {user_input} try some thing else")        


    # if user input not matches user looses a life out of six and when 0 game ends
    if user_input not in w_generated:
        lives -= 1
        if lives == 0:
            print("You Lose")
            end_state = True

    # printing the entered input
    print(f"{''.join(display)}")

    # in display list if there are no placeholders then we can declace the player as winner !!!
    if "_" not in display:
        print("You win !!!")
        end_state = True
    

    # used for printing ASCII Hangman states
    print(stages[lives])
