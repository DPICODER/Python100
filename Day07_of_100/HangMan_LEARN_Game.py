# The Game Rules 
"""
    The Player Has to Guess a word
    -   for Every unsucessfull Attemp a part of the body is drawn starting from head to Legs 
        if the whole body is drawn the man dies {You Lose}
    -   If all answers are Correct then You win
"""

# Step 1 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

list_words = ["cat","dog","mamooth","monkey","wolf","elephant"]

random_w_picker = random.choice(list_words)



lives = 6

eog = False

display = []  
print("The Word was : " + random_w_picker)



word_len = len(random_w_picker)

for letter in random_w_picker:
    display+="_"

print(display)

while not eog:

    user_input= input("Enter a letter to Check if it exists in the Word or Not :").lower()

    for pos in range(word_len):
        letter = random_w_picker[pos]
        if user_input == letter:
            display[pos] = letter

    if user_input not in random_w_picker:
        lives -= 1
        if lives == 0:
            eog = True
            print("You Lose")
            print("Your Man Got Hanged XD!!!!")

    print(f"{''.join(display)}")

    if "_" not in display:
        eog = True
        print("You win !!")

    print (stages[lives])