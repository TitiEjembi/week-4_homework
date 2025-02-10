#generate and display 6 unique random lottery numbers between 1 and 50
#which python data structure is best suited to store the numbers
#use the python help() function to find out which function to use from the python standard library called random.
#python help()
import random

#generating and displaying 6 unique random lottery numbers between 1 to 50

# number = 6 #number of random numbers to display
# #it ensures that there are no duplicate values in the output.
# lottery_numbers = random.sample(range(1,51),number)#using the random.sample method
# print(lottery_numbers)

#the random shuffle is another method that can be used.
lottery_numbers = list(range(1,51)) #lottery numbers from 1 to 50
random.shuffle(lottery_numbers) #using the shuffle method to shuffle the list from 1-50
lottery_numbers = lottery_numbers[:6] #to gey the 6 random numbers from the shuffled list
print(lottery_numbers)

#prefer the random.sample method