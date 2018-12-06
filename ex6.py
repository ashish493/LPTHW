types_of_people = 10
x=f"there are {types_of_people} types fo people"
# Here Variables are denoted a STRING value. NO BRACKETS FOR DECLARING ANY VARIABLE!!!!!!
binary="binary"
do_not="don't"
y=f" Those who know {binary} and those who {do_not}"
# Printing of a STRING value takes place
print(x)
print(y)
# STRING value of the variables(string) are used to print.
print(f" I said: {x}")
print(f" I also said '{y}'" )
hilarious= False
joke_evaluation= "Isn't that joke so funny?!{}" # HERE VARIABLE IS DECLARED FIRST THEN IT IS PRINTED UNLIKE IN ex7.py

# Here you learn that you can set the content of the format string 'later'
# by creating the format string in one variable yet specifying it's
# 'content/operator' at print time. Here the variable 'hilarious' is set as
# the format string at print time, which will output False in the final print.
# This seems powerful behaviour.
print(joke_evaluation.format(hilarious))

w= "This is a left side of ..."
e= "a string with a right side"
# Here 2 STRINGS are added so value will be joined
print(w+e)
