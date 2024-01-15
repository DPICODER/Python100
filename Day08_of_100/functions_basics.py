# Simple Function

def test_Fuction():
    print("The Fuction call Triggered")
    print("Running Fuction")
    print("Last Statement in function ,,,,Exiting Function\n\n\n")


test_Fuction()

# Function that allows input
## in a Function call with input the keywords in the actual function are parameters .
## the data || Value passed during function call are called Arguments.


def input_based_fn(name , age ,work):# passing params while calling the function.
    print(f"Hello There {name}")
    print(f"So You are {age} old i am glad to have you here")
    print(f"and You are a {work} Nice ! Nice!!\n\n\n")


#Positional Argumernt Matching
input_based_fn("Varun",23,"Student")# calling the function using Params as needed.
#Keyword Argument Matching
input_based_fn(age=21 , work= "Student" , name= "sai") # here the position of passing doesn't matter.
