# 3.8 Seeing the world

# Create a list and add five places that you would like to visit in the world.

dream_locations = []

# Adding locations to the list

dream_locations.append('vietnam')
dream_locations.append('usa')
dream_locations.append('russia')
dream_locations.append('china')
dream_locations.append('japan')

# Printing original list Order
print('This is the original order of the list:')
print(dream_locations)

# Using sorted() to print in alphabetical order
print('This is the list in alphabetical order')
print(sorted(dream_locations))

# Showing that the list is still in its original after having sorted it
print("This is the list back in it's original order")
print(dream_locations)

# Reversing the order of the list using the Reverse method

# Reversing the order of the list
dream_locations.reverse()
print("This is the list in reverse order")
print(dream_locations)

# Use reverse to return the list back to it's original order

dream_locations.reverse()
print("The list back in it's original order")
print(dream_locations)

# Sorting the list into alphabetical order and then reversing the order using sort

# Sorting dream_locations into alphabetical order
dream_locations.sort()

print("This is the list in alphabetical order")
print(dream_locations)

# Reversing the order of the list using sort

dream_locations.sort(reverse=True)

print("This is the list in reverse alphabetical order")
print(dream_locations)


# 3.9 Dinner guests
# Show how many people are coming to dinner using len()

# Creating the Dinner guest list
guest_list = []
guest_list.append('che guevara')
guest_list.append('doctor nick')
guest_list.append('cheif wiggum')
guest_list.append('bart simpson')

# Displaying the number of elements in the list
print(f"There are {len(guest_list)} guests coming for dinner.")


# 3.10 Every function
# Create a list of languages and use every function learned at least once on the list

languages = []
languages.append('english')
languages.append('spanish')
languages.append('french')
languages.append('russian')
languages.append('chinese')
languages.append('japanese')
languages.append('portuguese')

# Printing the original order of the list
print('Here is a list of languages')
print(languages)

# Sorting the list using sorted 

print('Here it is presented in alphabetical order')
print(sorted(languages))

# Printing the list in reverse alphabetical order

print('Here is a list of languages presented in reverse alphabetical order')
languages.sort(reverse=True)
print(languages)

# Recapping how many languages are in the list

# Storing the number of languages in a variable
og_lang = len(languages)
print(f'There are {len(languages)} languages currently in the list but I am about to add more.')

# adding more languages to the start middle and end of the list, arranging it in alphabetical order and then presenting the new ordered list.

languages.insert(0, 'flemish')
languages.insert(5, 'bulgarian')
languages.append('norweigan')

languages.sort()
print('Here is the list of languages in alphabetical order after having added some more languages to it:')
print(languages)
# Getting a lil bit cheeky here and experimenting with arithmetic in f strings.
print(f'There was {og_lang} languages in the list, {len(languages) - og_lang} more were added and now there are {len(languages)} languages in the list.')