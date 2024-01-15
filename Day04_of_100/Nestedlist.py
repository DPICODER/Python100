
# list 1 

fps_games = ["Pubg","Apex","CSGO","Finals","COD","Rainbow"]

# list 2
story_games = ["Assassin's Creed", "GTA" , "Baldurs Gate" , "Hitman", "TombRaider"]

#size of list 
fps_size = len(fps_games)
print(fps_size)
#getting last element of list

print(fps_games[fps_size-1])

# list 3
# Creating Nested list
games = [fps_games,story_games]

print(games)

# Here from gaems fpsgames = 0 and storygames = 1
# when user calls [1][1]
# from story games element at 1st index applies for all 
print(games[1][1])
print(games[0][1])
print(games[1][2])
