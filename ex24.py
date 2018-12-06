print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\that do.:')
print('\n new lines and \t tabs.')

poem="""
\t the lovely world
with logic so firmly planted
cannot discern \n needs of love
nor comprehend passion form intuition
and requires an explanation
\n\t\t where there is none.
"""

print("----------")
print(poem)
print("----------")


five=10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jelly_beans/100
    return jelly_beans,jars,crates


start_point=10000
beans,jars,crates,=secret_formula(start_point)

# Remember this is another way to format a string
print("With a starting point of: {}".format(start_point))
# Its just like with an f"" starting
print(f" we'd have {beans} beans , {jars} jars, and {crates} crates.")

start_point=start_point/10

print(" We can also do that in this way :")
formula= secret_formula(start_point)
# This is an easy way to apply a list of format string
print(" We'd have an {} beans ,{} jars and {} crates.".format(*formula))
