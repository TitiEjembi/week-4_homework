file_hand =open('pelican.text', 'a')
# file_hand is the file handle, which help to add functions to the file
# open function helps to Open file and return a stream
# 'a' means open for writing, appending to the end of the file if it exists

pelican = file_hand.write('A wonderful bird is the Pelican\n')
print(pelican)
# The method attempts to write the data to the underlying socket immediately.
pelican = file_hand.write('His bill holds more than his belly can\n')
print(pelican)
# The method attempts to write the data to the underlying socket immediately.

lines = ["He can take in his beak,\n" , "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
# The method writes a list (or any iterable) of bytes to the underlying socket immediately

output = file_hand.writelines(lines)
print(output)
# pelican .txt file is created and all the lines added through the .write method added to
# file handle, add the text to the pelican.text file