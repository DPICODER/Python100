# Capstone project a mix of all methods used form day 1 to 10

import random as rd 
import os 

def Welcome():
    """A Function with basic Introduction and User Requirements to play the GAME"""
    os.system("cls")
    print("Welcome to Black_Jack")
    if input("Press enter to continue")=="":
        user_balance = int(input("Enter the Amount you want to Gamble today : \n"))
        if user_balance <= 0:
            print("Enter a valid Amount")
            Welcome()
        else:
            Game_start(user_balance)
    else:
        print("Thanks for Checking out")


def Game_start(Amount):
    """The Actual Game Begins in this function"""
    place_bet = int(input("Enter the bet amount to begin the game values \n= 5 , 10 , 25 , 50 , 100 , 200 , 500 : "))
    if place_bet >=5:
        cards()
    else:
        print("Enter actual Amount from 5 , 10 , 25 , 50 , 100 , 200 , 500")    

user_sum = 0
system_sum = 0
def cards():
    global user_sum
    global system_sum
    print("Drawing Cards--")
    if input()=='y':
        user_sum += User_Draw_cards()
        system_sum += System_Draw_cards()

        if user_sum < 21 and user_sum > system_sum:
            if input("Do you want to draw again ? \n Enter 'y' yes \n Enter 'n' no")=='y':
                cards()
            else:
                print("You Win !!!!")
        elif system_sum < 21 and system_sum > user_sum:
            print("Syste, Wins !!!")
        else:
            print("It was a tie drawing cards again")
            cards()
    else:
        print("Great to Have you !!")
def User_Draw_cards():
    user_list=[]
    total = 0
    for i in range(0,2):    
        user_draw = rd.randint(1 , 10)
        user_list.append(user_draw)
    print(f"You have \n {user_list}")
    for val in user_list:
        total += val
    return val

def System_Draw_cards():
    system_list=[]
    total = 0
    for i in range(0,2):    
        system_draw = rd.randint(1 , 10)
        system_list.append(system_draw)    
    print(f"The system has \n [{system_list[0]},-]")
    for val in system_list:
        total += val
    return val

    
Welcome()