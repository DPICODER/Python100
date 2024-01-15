## LISTS in PYTHON

# Storing of Grouped peices of data each having connection with each other 
# example : states in India { storing the list of states in India }
# They are a Data-Structre to store mixed{numbers or Strings} or same data 
# In Python List is intitialized using : variable name = [ "Val1" , "Val2" , "Val3"]


states_of_India = ["Delhi" , "Maharastra" , "TamilNadu" , "JammuKashmir" , "WestBengal","Karnataka","MadyaPradesh","UttarPradesh"]

#Listing Starts from [0] beginning   to get last element we use [-1]from end

print(states_of_India[-1])

# print(states_of_India)

# to Modify data 

print(states_of_India)


states_of_India[0] = "New Delhi"

print(states_of_India[0])

# To add element to end of the list we use append function

states_of_India.append("Thiruvanathapuram")

print(states_of_India[-1])

states_of_India.extend([ "Telangana" , "AndhraPradesh" ,])

print(states_of_India)
