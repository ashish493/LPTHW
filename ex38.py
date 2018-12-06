ten_things="Apple oranges Crows  Telephone light sugar  "

print("Wait there are not 10 things in that lists. Let's Fix that ")

stuff=ten_things.split()
more_stuff=["day", "Night", "Song", "Frisbee",
             "Corn", "Banana", "Girl", "Boy"]

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1]) # whoa fancy
print(stuff.pop())
print(''.join(stuff)) # what cool!
print('#'.join(stuff[3:5])) # super stellar!
