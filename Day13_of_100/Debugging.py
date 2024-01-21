# Debugging in python or any coding refer's to solving or removing bug's from 
# our code 

# Example 1 
# Understand the logic
def func():
    #for i in range(1,20):# Here this block of code has a bug as range is 1,20 = 1,19 so 20 never comes
    for i in range(1,21):
        # here we dubugged our code by increasing the range by one to satisfy the condition
        if i == 20:
            print("Hello")

func()

# Example 2
# Reproduce the bug

from random import randint

dice_imgs = ["1️⃣","2️⃣","3️⃣"]
# dice_num = randint(1,3) # Here we face list index out of bound error at some point 
# to debug it we use range 0-2 as a list starts from 0 and ends at size - 1
dice_num = randint(0,2)
print(dice_imgs[dice_num])