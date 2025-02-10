#write a line of code to create a file handle to open and append to a file called pelican.txt

file_handle = open('pelican.txt', 'a') #opens the file in append mode

#Append the following line to the file using the write method of the file handle: A wonderful bird is the Pelican
chars_written = file_handle.write("A wonderful bird is the Pelican\n")

#append the following second line using the write method: "His bill holds more than his Belican"
chars_append = file_handle.write("His bill holds more than his Belican\n")

#creating a list and append the list using writelines method.
#the "\n" helps in starting a new line/ new sentence in the file.
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
file_handle.writelines(lines)