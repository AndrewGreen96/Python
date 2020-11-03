# 5.1 Conditional tests
# Write a series of conditional tests and print alongside them what the predicted outcome is.

bike = 'Honda'
print("Is bike == 'Honda'? I think this is True because both values being compared are equal.")
print(bike == 'Honda')

print("\nIs bike == 'honda'? I think this will return false because the variable bike holds honda with an uppercase first letter.")
print(bike == 'honda')

print("\nIf I use bike.lower() == 'honda' then it will return True because I have specified that the variable be compared in lowercase.")
print(bike.lower() == 'honda')

num_0 = 9
num_1 = 10
num_2 = 11
print("\nIs num_0 < 10? I think this will return True because 9 is in fact less than 10.")
print(num_0 < 10)

print("\nIs num_1 < 10? I think this will return False because 10 is not less than 10.")
print(num_1 < 10)

print("\nIs num_2 < 10? I think this will also return False because 11 is not less than ten but num_2 > 10 would return True.")
print(num_2 < 10)
print('num_2 > 10')
print(num_2 > 10)


# 5.2 More conditional tests
# Create a list of items and then test whether items are in the list and use if statements to evaluate the contents of the list

gear_teeth = []
gear_teeth.append(16)
gear_teeth.append(17)
gear_teeth.append(18)
gear_teeth.append(19)
gear_teeth.append(20)
gear_teeth.append(30)
gear_teeth.append(31)
gear_teeth.append(32)
gear_teeth.append(33)
gear_teeth.append(34)


for gear in gear_teeth:
    if gear <= 17:
        print(f'The {gear} tooth gear is normally used on a racing bike to go fast because the gear ratio is high.')
    elif 18 <= gear < 21:
        print(f'The {gear} tooth gear is also used on the rear hub but is considerably slower than the two gears above.')
    else:
        print(f'The {gear} tooth gear is usually a gear that is positioned on the crank rather than the hub because a bigger gear will make the smaller gear turn faster.')
        

