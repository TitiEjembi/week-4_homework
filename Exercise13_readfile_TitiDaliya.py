
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








#
# file_hand =open('pelican.txt', 'r')
# # file_hand is the file handle, which help to add functions to the file
# # open function helps to Open file and return a stream
# # 'r' means open for reading
#
#
# print('#'* 30, "SLURPING METHOD", '#'* 30)
# text = open('pelican.txt','r').read()
# print(text)
# # Read up to n bytes. If n is not provided, or set to -1,
# # read until EOF and return all read bytes
# # read method is reading the WHOLE pelican.txt file
# # print function print the values as the STRING
#
# text = open('pelican.txt', 'r').readlines()
# print(text)
# # .readline-Read one lines, where “line” is a sequence of bytes ending with \n.
# # .readlines() - Read and return the list of all logical lines remaining in the current file.
# # This updates the current line number to the last line of the file.
# # this method present the the lines of the pelican.txt as the list
#
# print(len(text))
# print(len(open('pelican.txt','r').readlines()))
# # use the len function to find out the number of items in the list
#
# for text in open('pelican.txt', 'r'):
#     # print(text[0:-1])
#     print(text[:-1])
# # applied the fore loop to iterate over the sequence and print using the index method
# # print text function gave the gaps in the line
# # used print function with indexes, which removed the spaces between the lines
#
#
#
#
