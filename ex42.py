## Animal is-a object(yes sort of confusing, look at extra credit)
class Animal(object):
    pass

## Dog is-a class(Animal)
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a init with name
        self.name=name

## Cat is-a class(Animal)
class Cat(Animal):

   def __init__(self,name):
       ## Cat has-a __init  with name
       self.name=name

## Person is-a object
class Person(object)

   def __init__(self,name):
       ## Person has-a init with name
       self.name=name

       ## Person has-a pet of some kind
       self.pet=None

## Employee is-a class(Person)
class Employee(Person):

   def __init__(self, name, salary):
       ## Employee has a init with name and salary  hmm what is this strange magic?
       super(Employee, self).__init__(name)
                          
