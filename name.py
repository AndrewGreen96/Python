name = "andrew green vellon"
print(name.title())
# The method title() applies title characters to all of the words in the variable 'name'.

first_name = "andrew"
last_name = "green vellon"
full_name = f"{first_name} {last_name}"
print(full_name.title())
# Here we can use the title method on full_name even though it does not directly contain any string information.

print(f"Hello, {full_name.title()}!")

# Simplifying further we get:

message = f"Hello, {full_name.title()}! This is all in one variable !"
print(message)