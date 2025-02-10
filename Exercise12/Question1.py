#what is wrong with the below? When you run the command, it takes the string 'oke'
# and runs it as single characters 'o' 'k' 'e'
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
#cheese += 'Oke'
#cheese.extend('oke') #+= the extend method does the same thing as the +=.
# However, if you add the brackets it would add the whole string
cheese.append(('oke'))
print (cheese)

#How should 'oke' be added to the end if the cheese list? to add the whole string to the list
#you need to add the brackets so it treats the strings as a whole
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['oke']
print (cheese)

#How would you add two new cheeses to the list with a single command.
#still using the += but adding the brackets to
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['oke', 'Brie', 'Mozzarella']
print (cheese)

#The append() method is a member of the list object, and it is used to modify
# the contents of an existing list by adding a new element to the end of the list
