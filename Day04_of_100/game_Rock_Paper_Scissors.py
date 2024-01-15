from turtle import position
import random

Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# RULES 
# Rock > Scissor
# Scissor > Paper
# paper > Rock
# if Same its a draw

game_dat = [Rock , Paper , Scissors]

system_inp = int(random.randint(0,2))

user_inp = int(input("Enter your choice \n 0.Rock \n 1.Paper \n 2.Scissor \n:"))

def printing(inp1,inp2):
    print("Your Choice : " + game_dat[inp1])
    print("System Played : " + game_dat[inp2])


if user_inp <= 2 and system_inp <=2 :
    if user_inp == 0 and system_inp == 1:
        printing(user_inp,system_inp)#Function Call
        print("You lose")
    elif user_inp == 1 and system_inp == 2:
        printing(user_inp,system_inp)
        print("You lose")
    elif user_inp == 2 and system_inp == 0:
        printing(user_inp,system_inp)
        print("You lose")
    elif user_inp == system_inp:
        printing(user_inp,system_inp)
        print("Draw Try Again ")
    else:
        printing(user_inp,system_inp)  
        print("You Win !!")
else:
    print("Enter input With in Range 0  , 1 , 2")



# game_numdat = len(game_dat)

# print(game_dat[game_numdat-1])