people=30
cars=40
trucks=15

# For dependent conditions like below we use elif.
# elif first checks first condition if it is false then it will move to other conditions.
# In if it checks all the conditions.
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print(" Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if cars>people and cars>trucks:
    print("What the F*** people are doing.")
