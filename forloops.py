# 4.1 Pizzas
# Create a list of my favourite pizzas and write a message that includes those pizzas using a for loop. 
# At the end write a message desribing how much you like pizza !

# Creating the list
pizzas = []

# # Populating the list
# pizzas.append('pepperoni')
# pizzas.append('four seasons')
# pizzas.append('fromagi')
# pizzas.append('margarita')
# pizzas.append('meat feast')
# pizzas.append('bbq chicken')

# # Printing the list to check it's been populated correctly
# print(pizzas)

# # Creating the for loop
# for pizza in pizzas:
#     print(f'The {pizza.title()} is one of my favourite pizzas and would recommend it to my friends.\n')
# print(f'I really love pizza but my favourite pizza is the {pizzas[4].title()}!')

# # 4.2 Animals
# # Add the names of some animals to a list and then finish off by writing what they all have in common

animals = []

animals.append('tazmanian devil')
animals.append('mouse')
animals.append('cat')
animals.append('coyote')
animals.append('dog')
animals.append('rabbit')

for animal in animals:
    print(f'The {animal} is a cute animal.\n')

print('One thing that all of these animals have in common is that they have appeared in popular childrens cartoons.')
print(f'My favourite is the {animals[0]} which appears in many Loony Toons cartoons as Taz, the tazmanian devil.')
