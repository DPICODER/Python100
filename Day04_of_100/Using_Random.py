import random


# for i in range (1,6):#printing till 5 iterations of Random Number

#     r = random.randint(1,21)
#     print("Random Number :",r)


# HEADS OR TAIL COIN TOSS 

random_side = random.randint(0,1)

if random_side == 1:
    print("The Outcome is HEADS")
else:
    print('The Outcome is TAILS')

# we can scale this for Generating OTP's, Games ,Password Generation and Etc.
     