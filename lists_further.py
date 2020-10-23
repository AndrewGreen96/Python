# 3.4 Guest List
# Create that includes the names of guests that you would invite to dinner and then send each of them a message inviting them to dinner.

guest_list = []
guest_list.append('che guevara')
guest_list.append('doctor nick')
guest_list.append('cheif wiggum')
guest_list.append('bart simpson')

invite_message = ', you have been invited to dine with me on the evening of the next full moon.'

print(f'{guest_list[0].title()}{invite_message}')
print(f'{guest_list[1].title()}{invite_message}')
print(f'{guest_list[2].title()}{invite_message}')
print(f'{guest_list[3].title()}{invite_message}')

# 3.5 Changing the guest list
# Replace one person from the list and add one person in their place then send out a new set of invitations.

# Stating the name of the guest that can no longer make the dinner.
uninvited_guest = 'bart simpson'
print(f'{uninvited_guest.title()} will no longer be attending the dinner.')

# Modifying the list such that the uninvited guest is replaced with the new guest will be attending in their stead.
guest_list[-1] = 'lisa simpson'

# Resending the invitations.
print(f'{guest_list[0].title()}{invite_message}')
print(f'{guest_list[1].title()}{invite_message}')
print(f'{guest_list[2].title()}{invite_message}')
print(f'{guest_list[3].title()}{invite_message}')

# 3.6 More Guests
# Inform your guests that you have found a bigger table and that more guests will be attending because of this.
# Add one person to the beginning of the list, one to the middle of the list and one onto the end of the list and then resend invitations to all of the guests that are now on the list

# Informing the guests that more people people will be attending the dinner.
print('I have found a bigger table. Owing to this there will be more guests joining us for dinner.')

# Adding people to the guest list.
guest_list.insert(0, 'homer simpson')
guest_list.insert(3, 'marge simpson')
guest_list.append('sideshow bob')

# Resending the invites to all of the guests.
print(f'{guest_list[0].title()}{invite_message}')
print(f'{guest_list[1].title()}{invite_message}')
print(f'{guest_list[2].title()}{invite_message}')
print(f'{guest_list[3].title()}{invite_message}')
print(f'{guest_list[4].title()}{invite_message}')
print(f'{guest_list[5].title()}{invite_message}')
print(f'{guest_list[6].title()}{invite_message}')

# 3.7 Shrinking guest list.
# Send a message to your guests informing them that the table will not be arriving in time for the dinner and that you will only have 2 available seats for guests.
# Then send all of the guests that have been univited a message apologising for the inconvenience and send the two guests that are still invited a message letting them know they are still invited.
# Delete the last two guests from the list and print the list to prove that there are no more guests left on the list.

# Informing the guests that the table won't be arriving in time.
print('I am sorry to inform you that the table will not be arriving in time for the dinner and that some of you will be univited because of this.')

#Assigning the apology to a variable.
apology = ', I am sorry to inform you that you have been uninvited from the guest list. I hope to see you next time.'

#Popping guests from the list such that only two guests remain and then sending the popped guests an apology.
popped_guest = guest_list.pop()
print(f'{popped_guest}{apology}')

popped_guest = guest_list.pop()
print(f'{popped_guest}{apology}')

popped_guest = guest_list.pop()
print(f'{popped_guest}{apology}')

popped_guest = guest_list.pop()
print(f'{popped_guest}{apology}')

popped_guest = guest_list.pop()
print(f'{popped_guest}{apology}')

# Sending the two remaining guests a message letting them know that they are still invited.
message = ', you are still invited to dinner I hope to see you there!'

print(f'{guest_list[0].title()}{message}')
print(f'{guest_list[1].title()}{message}')

# Removing the last two guests from the guest list and printing the empty guest list to ensure that there are no guests left on the list.
del guest_list[0]
del guest_list[0]

print(guest_list)