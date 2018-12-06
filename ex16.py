from sys import argv

script,filename=argv

print(f"we are going to erase{filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you want that hit RETURN")

input("?")

print("Opening the file...")
target=open(filename, "w")
# 'w' is an arguement that puts open() into write mode. It opens by default to
# read mode so to allow write later, you need to set the write flag when you
# actually open the file object. A file object without 'w' can't be written to.
# CAUTION - using 'w' will truncate the file if it already exists!!
print("t=Truncating the file... GoodBye !!!")
# Truncate basically deletes the contents of the file, be careful!
target.truncate()
# Truncate basically deletes the contents of the file, be careful!
# The following line is not necessary, opening the file with the 'w' argument
# will truncate the file anyway if the file exists, and if it doesn't then it
# would be blank anyway.

print("Now I'm going to ask you for three lines.")

line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")

print("I'm going to write these to file")
# This writes the content of a variable and then a new line over and over
# again in order to format the text in the new file.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# FOR MULTIPLE LINES IN ONE LINE TYPE:  target.write('{}\n{}\n{}\n'.format(line1, line2, line3))
print("And finally we close it")
target.close()
