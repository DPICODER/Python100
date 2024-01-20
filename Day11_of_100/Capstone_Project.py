# Black_Jack beta v 0.1 
#Capstone project a mix of all methods used form day 1 to 10

import random
import os

def welcome():
    """Greetings Funtion and Gamestart invoker"""


    print("Welcome to BLACK_JACK V 0.1")
    if input("Press Enter to continue")=="":
        gamestart()
    else:
        welcome()

def card_sum(cards):
    """used for evaluating the total of the user and system cards"""
    if sum(cards)>21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)



def gamestart():
    """The Game function"""
    os.system("cls")
    is_game_over = False
    user_cards = []
    sys_cards = []

    for _ in range(2):
        user_cards.append(card_drawer())
        sys_cards.append(card_drawer())

    while not is_game_over :    
        user_score = card_sum(user_cards)
        sys_score = card_sum(sys_cards)

        print(f"Your Cards are :{user_cards} , CurrentScore is : {user_score}")
        print(f"System First Card is :{sys_cards[0]}")


        if user_score == 0 or sys_score == 0 or user_score >21:
            is_game_over = True 
        else:
            user_repeats = input("Type 'y' to get another card  ,  Type 'n' to pass : ")
            if user_repeats == "y":
                user_cards.append(card_drawer())
            else:
                is_game_over = True

    while sys_score != 0 and sys_score <17:
        sys_cards.append(card_drawer())
        sys_score = card_sum(sys_cards)
    # os.system("cls")
    print(f"\n\nYour Final Cards : {user_cards} \nYour Final Score is : {user_score}")
    print(f"\nSystem's Final Cards : {sys_cards} \nSystem's Final Score is : {sys_score}")

    print(compare(user_score , sys_score))

    if input("Do you wanna play another  game of BlackJack? Type 'y' or 'n' ")=='y':
        gamestart()
    else:
        print("Thaks For Playing BlackJack")
        is_game_over = True




def card_drawer():
    """function for drawing deck of cards form the cards list"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card_no = random.choice(cards)
    # print(card_no)
    return card_no


    
def compare(user_score,sys_score):
    """Function for Comparing User_Score and Systems_Score"""

    if user_score == sys_score:
        return "\nITS A DRAW \n"
    elif sys_score == 0:
        return "\nLOSE , Opponent Has a BLACKJACK\n"
    elif user_score == 0:
        return "\nYou Win BLACKJACK\n"
    elif user_score >21:
        return "\nYou Lose , Went Over 21\n"
    elif sys_score > 21 :
        return "\nYou Win , Opponent Went over 21\n"
    elif user_score > sys_score:
        return "\nYou Win !!!"
    else:
        return "\nYou Lose\n"

   






# first function call begins here v        
welcome()


