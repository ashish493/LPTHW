the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

# this is first of a kind of for-loops goes through the list
for number in the_count:
    print(f"this is count {number}")

# same as above
for fruits in fruits:
    print(f"A fruit of type: {fruits}")

# also we can go through mixed lists too
# notice we have to use {}, since we don't know wht is in it.
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one.
elements=[]

# The use the range function that lists too.
for i in range(0,6):
    print(f"adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# Now we can print them too.
for i in elements:
    print(f"Element was : {i}")
