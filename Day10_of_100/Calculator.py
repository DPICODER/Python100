# Calculator
import os
#Adding
def add(n1,n2):
    return n1 + n2

#Subtracting
def sub(n1,n2):
    return n1 - n2

#Multiplying
def mul(n1,n2):
    return n1 * n2

#Deviding
def div(n1,n2):
    return n1 / n2

operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}


def Calculator():
    """A Fuction build for simple calculation based on Recursion and function calls for 2 or More Numbers"""
    os.system("cls")
    to_continue = True
    num1 = float(input("Enter a First Number ?:"))
    for ops in operators:
        print(ops)

    while to_continue:
        symbol = input("Pick a symbol to perform Operation from Above : ")
        num2 = float(input("Enter a Next Number ?:"))
        Calc_func = operators[symbol]
        inital_ans = Calc_func(num1,num2)
        print(f"\n\n---->>{num1} {symbol} {num2} = {inital_ans}")
        print("\nDo You Want to Continue ?")
        decision = input("Enter .: \n 'y' -> to continue \n 'n' -> to perform new calculation \n 'x' -> to Exit\n:")
        if decision=="y":
            num1 = inital_ans
        elif decision =="n":
            Calculator()
        else:
            to_continue = False


Calculator()