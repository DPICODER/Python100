names = ["Ramesh" , 'Suresh' , 'Somesh' , 'Mallesh' , 'Komtesh' ,' Ganesh' , 'Ganpath' , 'Yeeda ',' Kuara' ,' Moteya' ,' Motabhai']

import random 

num_items = len(names)

random_choice = random.randint(0,num_items-1)

selected_Person = names[random_choice]

print(selected_Person+" is The One paying Bill Today")

