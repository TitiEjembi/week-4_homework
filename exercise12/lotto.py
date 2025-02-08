import random
# random variable generator

for i in range(6):
    num =random.randint(1,50)
    print(num)
# tried to create a for loop to iterate over the elements of the sequence of numbers
# range created to have fix the numbers of attempts to  return a new object
# used randint method on random function to generate random integer with a start and end point provided
# numbers generated in this form was random integers which did not belong to a collection

numbers = [random.randint(1,50) for i in range(6)]
print(numbers)
# in this method assigned the value of .randint method to  a variable called numbers
# variable numbers has collection of numbers in the form LIST

numbers_1 ={random.randint(1,50) for i in range(6)}
print(numbers_1)
# in this method assigned the value of .randint method to  a variable called numbers
# variable numbers has collection of numbers in the form SETS

start= 1
end=50
chances=6
lotto_nums = [random.randint(start,end) for i in range(chances)]
print(lotto_nums)
# used the same method of randint and passed it to a new variable called lotto_nums
# tried to automate the process to get same results for any starting
# and ending numbers and range of numbers

