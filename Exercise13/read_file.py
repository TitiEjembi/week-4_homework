#use the open and read methods to slurp the entire contents of your pelican.txt.file
#display the type of the returned data and print the contents of the returned data
#what data type is the output?
#now write some code that will read the pelican.txt file into a list and then output the number of items within the list
#now use a loop to iterate over and print the contents of the file. be sure not to include any blank lines in the output.

#open and read methods to slurp the entire contents
#using the f string to indicate the ..

song_content = open('pelican.txt', 'r').read()

print(type(song_content))
print(f"entire content:\n{song_content}")
#what data type is the output? strings?

#write some code that will read the pelican.txt file into a list and then output the number of items within the list.
#use the lens method
song_content = open('pelican.txt', 'r').readlines()
number_of_items = len(song_content)
print(song_content)
print(number_of_items)


#now use a loop to iterate over and print the contents of the file. be sure not to include any blank lines in the output.
for item in song_content:
  if item.strip() != '': #Return a copy of the string with leading and trailing whitespace removed
    print(item.strip())
    # if item is an empty string, do not print it




