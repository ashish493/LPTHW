cars = 100
space_in_a_car = 4.0
drivers = 30
# space between operators is good becoz it is easy to read
passengers = 90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_peassagenger_per_car=passengers/cars_driven
# _(underscore is used in variable alternatives to spacebar)
# variables are defined before and then used
print("there are",cars,"cars  available")
print("there are",drivers,"drivers available")
print("there will be",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today")
print("we have",passengers,"to carpool today")
print("we need to about",average_peassagenger_per_car,"in each car")
