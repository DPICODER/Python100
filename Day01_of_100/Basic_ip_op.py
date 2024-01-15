# Basic Printing and getting User input

print("Wassup ! new to Python")


# Storing the user inputted data into the variable for later use in the scope 
val = input("Enter your name : ")

val2 = input("now enter your Dogs name for security verification : ")

#printing the both variables using f printing method to include multiple variables at once
print(f"So your name is ",val," and You have a Dog named ",val2)


#Taking input and printing the input with a print message at the same time 

print("So You are :" + input("Whats your age :"))


#Output : 
		# Wassup ! new to Python
		# Enter your name : Varun
		# now enter your Dogs name for security verification : Brownie
		# So your name is  Varun  and You have a Dog named  Brownie
		# Whats your age :24
		# So You are :24


#problem-1
# Take user name using input function and return the no of letters in the name 

print(len(input("Enter your FULL-NAME : ")))

#problem-2
# Take user input for two variables and swap those variable and print swapped data

a = input("Enter a value :")
b = input("Enter b value :")

print("Before swapping")
print("a :"+a)
print("b :"+b)

# using temp for a temporary container var for swapping purpose

temp = a 
a = b 
b = temp 

print("After swapping")
print("a :"+a)
print("b :"+b)
