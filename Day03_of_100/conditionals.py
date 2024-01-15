# conditions in the python work as same as the common programming conditional statements like
# if else elif 

# example

print("Age based Categorizer")

name = input("Enter your name :")

age_inp = input("Enter your age :")

age= int(age_inp)

if age < 8:
	print("You are Categorized as a Child")
elif age < 15 and age > 8:
	print("You are Categorized as a Teen")
elif age > 15 and age < 35:
	print("You are Categorized as a Adult")	
elif age >35 and age <60:
	print("You are Categorized as a Elder")
else:
	print("Damnn You are still alive Keep Goin Mannn......")

print("Do You wish to continue the program Execution: [Y / N]")
inp = input()

if inp == "Y" or inp =="y":
	print("OK lets continue :")
	print("Here are some thigs you can do as you are ",age)
	print("Lets play a game")
	print("Start...........")
	score = 0

	if age < 8:
		print("What is the name of our planet")
		ans=input()
		
		if(ans == 'earth' or ans =='Earth' or ans =='EARTH'):
			print("Rigth answer !!!")
			score += 1
			print("Your score is :",score)
		
		else:
			print("Nice Try But it was Wrong")

		print("How many days are in a week ?")
		ans=input()
		if(ans == 7 or ans ==ans =='seven' or ans =='Seven' or ans =='SEVEN'):
			print("Rigth answer !!!")
			score += 1
			print("Your score is :",score)
		else:
			print("Nice Try But it was Wrong")

		if(score == 2):
			print("Congratulations You are the Winner")
		else:
			print("You lose no Problem Try next time")
else:
	print("See You then Bye -------")