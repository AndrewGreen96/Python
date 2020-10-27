# 4.3 Counting to twenty
# Use a for loop to print the numbers from 1 to 20.

for number in range(1,21):
    print(number)


# 4.4 One million
# Make a list from 1 to 1,000,000 and use a for loop to print it

big_list = list(range(1,1000001))
print(big_list)


# 4.5 Summing to one million
# Create a list from one to one million, use min() and max() to check that it starts at 1 and ends at 1000000 and then sum all of the elements from the list together.

onemillion = list(range(1,1000001))
print(min(onemillion))
print(max(onemillion))
print(sum(onemillion))


# 4.6 Odd numbers 
# Make a list of the odd numbers from 1 to 20 and use a for loop to print each number.

odd_numbers = list(range(1,21,2)) 
for odd in odd_numbers:
    print(odd)
print('\n')

# 4.7 Threes 
# Make a list of the multiples of 3 from 3 to 30 and then print it.

threes =list(range(3,31,3))
for number in threes:
    print(number)


# 4.8 Cubes
# Make a list of the first 10 cubes.

cubes = list(range(1,11))
for cube in cubes:
    print(cube**3)


# 4.9 Cube comprehension
# Use a list comprehension to generate a list of the first 10 cubes.

cubes =[cube**3 for cube in range(1,11)]

