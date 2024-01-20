############ SCOPE ############

# Example 
# Here Enemies is a Global Scope and it can be accessed any where in this whole code and they are not bounded by function scope
enemies = 1
print("\n Local Scope")

def increase_enemies():
    enemies = 2
    print(f"Enemies inside Function are : {enemies}")

increase_enemies()
print(f"Enemies Outside the Function are : {enemies}")


# Local Scope

def drink_potion():
    # Local scope due to it's inside the Fuction which has boundary with in the function
    potion_speed = 2
    # print(potion_speed)

drink_potion()

#The Below line gives a error as its outside the function and not reachable by scope Try Uncommenting it and Running it
# print(potion_speed)
game_level = 3
def create_enemy():
    enemies = ["Skeleton","Zombie","Alien"]

    if game_level < 5 :
        new_enemy = enemies[0]

    print(new_enemy)

# Global Scope 

# Modifying Global Scope
enemies = 1
print("\n Global Scope")
def increase_enemies():
    # global enemies # Using global keyword inside the function we can access the variable from within the function
    
    print(f"Enemies inside Function are : {enemies}")
    # But Rather than using Global Keyword which may Create Bug's in the Long Run we use Return Keyword
    return enemies + 2

enemies = increase_enemies()
print(f"Enemies Outside the Function are : {enemies}")

# Global Scope can be used for declaring Constants like pi , area formual ,url etc