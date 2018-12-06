# Create a mapping of state to abbrevation
states={
 'Oregon':'OR',
 'Florida':'FL',
 'California':'CL',
  'New York':'NY',
  'Michigan':'MI'
}

# cREATE A BASIC SET OF STATES AND SOME CITIES IN THEM
cities={
 'CA':'San Franscico',
 'MI':'Detroit',
 'FL':'Jacksonville'
}

# Add some new citites
cities['NY']='New York'
cities['OR']='Portland'

# Print out some cities
print('_'*10)
print('NY State has:',cities['NY'])
print('OR State has:',cities['OR'])

# print some states
print('_'*10)
print("Michigan's abbrevation is:", states['Michigan'])
print("Florida's abbrevation is",states['Florida'])

# do it by using the state then cities dict
print('_'*10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#Print every state
print('_'*10)
for state,abbrev in list(states.items()):
    print(f"{state}is abbrevated {abbrev}")

  # print every city in states
print('_'*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('_'*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbrevated {abbrev}")
    print(f" and has city {cities[abbrev]}")

print('_'*10)
# safely get a abbrevation by state that might not there
state=states.get('Texas')

if not state:
    print("Sorry , no Texas")

# get a city with a default value
city=cities.get('TX','Does Not Exist')
print(f"The city for state 'TX' IS :{city}")
