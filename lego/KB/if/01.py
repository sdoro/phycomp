from spike import PrimeHub

hub = PrimeHub()                  # this is an object

# Conditions

# < less than
# > more than
# == equal to
# >= more than or equal to
# <= less than or equal to
# != not equal to
# and
# or

# Age checking program

age = 10
if age >= 18:
    hub.light_matrix.write('you can drive')
else:
    hub.light_matrix.write('you are too young to drive')
