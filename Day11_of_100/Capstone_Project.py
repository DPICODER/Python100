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

def gamestart():
    """The Game function"""
    os.system("cls")
    card_store()

def card_drawer():
    """function for drawing deck of cards form the cards list"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card_no = random.choice(cards)
    # print(card_no)
    return card_no


def card_store():
    """ function for storing the user/sys drawn cards in a list"""
    user_cards = []
    sys_cards = []
    for i in range (2):
        user_cards.append(card_drawer())
        sys_cards.append(card_drawer())

    print(user_cards)
    print(sys_cards)

    card_sum(user_cards , sys_cards)

                                 #|  

def card_sum(user , sys):
    """used for evaluating the total of the user and system cards"""
    print("User Cards : ",user)
    print(sum(user))




# first function call begins here v        
welcome()


