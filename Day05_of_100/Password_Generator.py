import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%' , '&' , '(', ')', '*', '+']


print("Welcome to PyPassGen")
user_inp_letters = int(input("How many letters would you like to have in Your Pass : \n"))
user_inp_Numbers = int(input("How many Numbers would you like to have in Your Pass : \n"))
user_inp_Symbols = int(input("How many Symbols would you like to have in Your Pass : \n"))


cryper = [letters,numbers,symbols]

letters_size = len(letters)
numbers_size = len(numbers)
symbols_size = len(symbols)

final_password = ""

# Eazy level
# for password in range(user_inp_letters+1):
#     random_char = random.choice(letters)
#     final_password += random_char
# for password in range(user_inp_Symbols+1):
#     random_char = random.choice(symbols)
#     final_password += random_char
# for password in range(user_inp_Numbers+1):
#     random_char = random.choice(numbers)
#     final_password += random_char



#Hard Level

password_list = []

for password in range(user_inp_letters+1):
    password_list.append(random.choice(letters))
for password in range(user_inp_Symbols+1):
    password_list.append(random.choice(symbols))
for password in range(user_inp_Numbers+1):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)
# print(password_list)

for val in password_list:
    final_password += val

print("The Generated Secure Password is : | "+final_password + " | ")
