# Calculator

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



num1 = int(input("Enter a First Number ?:"))
num2 = int(input("Enter a Second Number ?:"))

for ops in operators:
    print(ops)

symbol = input("Pick a symbol to perform Operation from Above : ")

Calc_func = operators[symbol]

print(f"The {num1} {symbol} {num2} = {Calc_func(num1,num2)}")