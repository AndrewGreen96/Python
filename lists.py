# Task 3.1 Names
# Store the names of a few of your friends in a list called names.
# Print each person's name by accessing each element in the list, one at a time.
names = ['george', 'taylor', 'elaine']
print(names[0].title())
print(names[1].title())
print(names[-1].title())

# Task 3.2 Greetings
#  Print a message to each person in the list created in 3.1. The message should be the same for everyone and should include their own respective names.

message = ', this is a personalised message just for you.'

print(f'{names[0].title()}{message}')
print(f'{names[1].title()}{message}')
print(f'{names[-1].title()}{message}')

# Task 3.3 My own list
# Create a list of motorcycle brands and print a series of statements about them.

moto_names = ['honda', 'kawasaki', 'ducati', 'ktm', 'aprilia', 'yamaha', 'suzuki']

print(
    f'The MotoGP has been really good this year because factory teams like {moto_names[0].title()} have not been doing so well owing to the fact that they are missing their main rider due to injury. Other teams such as {moto_names[-1].title()} and {moto_names[3].upper()} have been shining and showing off more potential this year as a result of this.'
)

# Note: Are line breaks a thing in Python...?