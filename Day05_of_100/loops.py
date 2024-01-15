fps_games = ["pubg","csgo","apex","cod","finals"]

for games in fps_games:
    print(games.upper())


total = 0

for num in range(1,201):
    total += num

print(total)

# sum of all even numbers

user_inp = int(input("Enter a Range :"))

total = 0
for num in range(user_inp+1):
    if num % 2 == 0:
        total = total + num

print(total)

# fizz buzz game 
# if divisible by 3 print fizz
# if divisible by 5 print buzz
# if divisible by 3 and 5 print fizzbuzz


u_inp = int(input("Enter a range :"))

for n in range(u_inp+1):
    if n % 3==0 and n % 5==0:
        print("Fizz Buzz")
    elif n % 3==0:
        print("Fizz")
    elif n % 5==0:
        print("Buzz")
    else:
        print(n)