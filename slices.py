# 4.10 Create a list and then print the top three items from it, 2 items from the middle of the list and then the bottom three items of the list.

car_brands = []

car_brands.append('honda')
car_brands.append('toyota')
car_brands.append('triumph')
car_brands.append('ford')
car_brands.append('mini')
car_brands.append('bmw')
car_brands.append('mercedes')
car_brands.append('lexus')


print('The top three car brands are:')
print(car_brands[:3])

print('\nA few of the car brands from the middle are:')
print(car_brands[2:5])

print('\nThe car brands that are the end of the list are the following:')
print(car_brands[5:])


# 4.11 My pizzas, your pizzas
# Make a copy of the original pizzas list and call it friends_pizzas

pizzas = []

pizzas.append('pepperoni')
pizzas.append('four seasons')
pizzas.append('fromagi')
pizzas.append('margarita')
pizzas.append('meat feast')
pizzas.append('bbq chicken')

# Making a copy of the list

friends_pizzas = pizzas[:]

# a) Add a pizza to the original list
# b) Add a different pizza to the new list
# c) Create a message for your favourite pizzas and your friends favourite pizzas respectively


# Adding pizzas to both of the lists
pizzas.append('meteor')
friends_pizzas.append('vegan')

# Creating the output messages

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print('\nAnd these are my friends favourite pizzas:')
for fpizza in friends_pizzas:
    print(fpizza.title())


# 4.12 More loops
# Create two more food related lists and print them using for loops

# Populating the list

naans = []

naans.append('plain')
naans.append('keema')
naans.append('peshwari')
naans.append('chicken tikka')
naans.append('garlic')
naans.append('garlic and spice')

doughnuts = []

doughnuts.append('ring')
doughnuts.append('jam')
doughnuts.append('custard')
doughnuts.append('chocolate')
doughnuts.append('boston creme')
doughnuts.append('white chocolate')
doughnuts.append('raspberry filled')

print("\n\nI've collected a few of my favourite naans and doughnuts...")
print('But my top three doughnuts are')
for doughnut in doughnuts[4:]:
    print(doughnut.title())

print('\nand my top 3 naans are:')
for naan in naans[1:4]:
    print(naan.title())