import random 

LEVEL_EASY = 10
LEVEL_HARD = 5

def check(guess , answer , turns):
    if guess < answer:
        print( "Too Low" )
        return turns - 1
    elif guess > answer:
        print( "Too High")
        return turns - 1
    else:
        print( "Right Answer's")



def set_difficulty():
    level = input("Choose a difficulty , Type 'easy' or 'hard' ")
    if level == "easy":
        return LEVEL_EASY
    else:
        return LEVEL_HARD
    
def game():
    print("Welcome To Number Guessing Game")
    print("System is Picking a Number ....")
    answer = random.randint(1,100)
    print(f"the predicted answer is {answer}")
    guess = 0
    turns = set_difficulty()
    while guess != answer:
        print(f"You have {turns} remaining to Guess the Number ")
        guess = int(input("Make a guess : "))
        turns = check(guess=guess , answer= answer,turns=turns)
        if turns == 0:
            print("You run out of Guesses You lose")
            return
        elif guess != answer:
            print("Guess Again...")


game()


















# number = random.randint(1,100)

# difficulty = input("Enter Difficulty Type 'easy' or 'hard' ")

# if difficulty == "easy":
#     level = 10
# else:
#     level = 5 
# print(f"The sys no is : {number}")
# while level != 0:
#     value = int(input("Guess a Number : "))
#     if value < number:
#         level -=1
#         print("\nToo Low")
#         print(f"Wrong Answer You have {level} no of Attempts\n")
#     elif value > number :
#         print("\nToo High")
#         level -=1
#         print(f"Wrong Answer You have {level} no of Attempts\n")
    
#     elif value == number:
#         print(f"\n\nYou Guessed a correct Number it was {number}\n\n")
#         level = 0
#     else:
#         print("\n\nEnter a valid Number in 0 - 100 range\n\n")
        
