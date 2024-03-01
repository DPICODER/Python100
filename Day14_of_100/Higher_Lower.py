data = [
    {
        'Name': 'Instagram',
        'Follower': 400,
        'description':'social_Media',
        'country':'USA'        
    },
    {
        'Name': 'CR7',
        'Follower': 380,
        'description':'Footballer',
        'country':'Portugal'        
    },
    {
        'Name': 'Leo Messi',
        'Follower': 360,
        'description':'Footballer',
        'country':'Argentina'        
    },
    {
        'Name': 'Virat Kohli',
        'Follower': 320,
        'description':'Cricketer',
        'country':'India'        
    },
    {
        'Name': 'RameshBD',
        'Follower': 200,
        'description':'Influencer',
        'country':'India'        
    },
    {
        'Name': 'Gardon Ramsay',
        'Follower': 180,
        'description':'Chef',
        'country':'USA'        
    },
    {
        'Name': 'Shroud',
        'Follower': 160,
        'description':'Gamer',
        'country':'USA'        
    },
    {
        'Name': 'Minecraft',
        'Follower': 150,
        'description':'Company',
        'country':'USA'        
    },
    {
        'Name': 'MSD',
        'Follower': 120,
        'description':'Cricketer',
        'country':'India'        
    },
]


import random
import os 

# Function to format account data for printing
def format_dat(acc):
    '''Formats the randomly generated account data into a structured string for printing on the console'''
    acc_name = acc["Name"]
    acc_desc = acc["description"]
    acc_country = acc['country']
    return f"{acc_name}, a {acc_desc} from {acc_country}"

# Function to check user's guess
def check_user_pick(guess , a_dat , b_dat):
    '''Checks whether the user guessed the right answer based on both options'''
    if a_dat > b_dat:
        return guess == "a"
    else:
        return guess == "b"

score = 0
should_cntd = True

# Initializing account_b for global data to get data of randomly generated account 
acc_b = random.choice(data)

while should_cntd:
    # Loop runs until answer is wrong

    # Storing account_b in acc_a and generating new acc_b
    acc_a = acc_b
    acc_b = random.choice(data)
    
    # Ensure acc_b is different from acc_a
    while acc_a == acc_b:
        acc_b = random.choice(data)

    # Printing formatted data for comparison
    print(f"A . Compare {format_dat(acc_a)}")
    print(f"B . Compare {format_dat(acc_b)}")

    # Retrieving follower count from data
    a_Follower= acc_a["Follower"]
    b_Follower= acc_b["Follower"]

    # User input for guess
    guess = input("Who has More Follower A or B : ").lower()

    # Function call to verify user input / choice
    is_correct = check_user_pick(guess=guess, a_dat=a_Follower, b_dat=b_Follower)

    # Increment score if correct or exit game if wrong
    if is_correct:
        os.system('cls')  # Clearing screen
        score += 1
        print(f"Right !! You Are Correct , Current score = {score}")
    else:
        should_cntd = False 
        print(f"Oops! You are wrong. Total score = {score}")

