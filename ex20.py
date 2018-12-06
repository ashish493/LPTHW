# Imports the argv function (?) from the sys library
from sys import argv
# sets up 'argv' to accept the script and 'test.txt' file as input
script, input_file=argv
# Creates a function 'print_all(f)' which reads and prints the input
def print_all(f):
    print(f.read())
# Creates a function 'rewind(f)' which sets the input files current position
# to 0 via the 'seek()' function (this is in bytes i.e the start of the file)
def rewind(f):
    f.seek(0)

# Creates a function that accepts an integer (in this case from 'current_line')
# denoting the line to read and then reads that line with the 'readline()'
# function.
# NOTE - readline() reads a single line up to the \n character but leaves the
# \n character at the end of the line, so this automatically advances the file
# position by 1 line for every time the function is called and leaves a blank
# newline in place. That why there's a line break in the output code.
# That's how this script is reading, printing and advancing each line in turn

def print_a_line(line_count,f):
    print(line_count,f.readline())
# Sets 'current_file' to equal the file object 'input_file', which is defined
# in the arguments when running the script, in this case it's 'test.txt'
current_file=open(input_file)
# Prints the whole file on a newline under the print statement
print("First let's print the whole file: \n")
# Calls the function 'print_all' using 'current_line' as the parameter
print_all(current_file)

print("Now let's rewind, kind of a like a tape.")

# Calls the function 'rewind()' with the parameter 'current_file' which should
# reset the files current position to 0, i.e. to the beginning.
# I'm guessing this is needed because we already read/printed the whole
# file so the current position is the end of the file.
# UPDATE - commenting out the line below and running the script doesn't print
# the lines out, which would suggest the files current position  at this
# point in the script is at the end of the file.

rewind(current_file)

print("let's print three lines:")
# Sets variable 'current_line' to 1
current_line=1
# Calls function 'print_a_line()' with 'current_line' and 'current_file' as
# parameters.
print_a_line(current_line, current_file)
# Calls function 'print_a_line()' with 'current_line' and 'current_file' as
# parameters. 'current_line here being set to 'current_line + 1' which is
# equivalent to '1 + 1'.
current_line=current_line+1
print_a_line(current_line, current_file)
# Calls function 'print_a_line()' with 'current_line' and 'current_file' as
# parameters. Again 'current_line' is incremented by 1.
current_line=current_line+1
print_a_line(current_line, current_file)
