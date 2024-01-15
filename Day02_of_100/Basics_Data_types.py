# Data Types 

# auto assignment based on data 

# Integer , String , Float , Boolean

a = str(123)
print(a)
print(type(a)) # used for checking data type of a variable

b = float("123")
print(b)
print(type(b))

c = int("34")
print(c)
print(type(c))

print(6/3)
print(int(6/3))


# Body mass index Calculator

# formula =   BMI = weight(kg) / height^2

height = input("Enter Height :")
weight = input("Enter Weight :")

weight_integer = int(weight)
height_float = float(height)

bmi = weight_integer/ (height_float * height_float) 
bmi_as_int = int(bmi)
print(f"Your BMI is : {bmi_as_int}")



# Rounding in PY 
print(8/3)

print(round(8/3))

# floor division 

print(8//3)

# Problem remaining span

age = input("Enter your age :")

years = 65 - int(age)

weeks = years * 52

print(f"You have {weeks} weeks left")