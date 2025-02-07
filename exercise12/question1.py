cheese =['Cheddar', 'Stilton', 'Cornish Yarg']
# a variable assigned the value of list of strings

# cheese += 'Oke'

# we are trying to add a string to the list string using ASSIGNMENT OPERATOR
# hence it has taken each element as the string and added them to the list as separate string
# WHAT'S WRONG: trying to add a 'string' to a list without using appropriate methods
print(cheese)

# how to add 'Oke' to add at the end
# METHOD 1. using assignment operator to add list to list
cheese += ['Oke']
print(cheese)

# METHOD 2. using the .extend method to add an iterable list
cheese.extend(['Oke'])
print(cheese)

# Method 3. using the .append method to add ONLY ONE item at the end of the list
# we cannot assign a variable with the append method as it returns NONE
cheese.append('Oke')
print(cheese)

# how to add two new items with single command
cheese.extend(['Gouda', 'Edam'])
print(cheese)