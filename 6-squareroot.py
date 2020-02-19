
# This imports the newton_root function from the module functions.py
from functions import newton_root

# This takes in input from the user, converts 
# it to float and gets the absolute value so that 
# strings will not be accepted and it will
# be strictly positive
pos= abs(float(input("Please enter a positive number: ")))

# This applies the Newton_Raphson method for finding square roots
# for 5 iterations (should be sufficiently accurate for 1 decimal place)
# and rounds the result to 1 decimal place using the round function
pos = round(newton_root(pos, 5), 1)

# This prints the result to the screen
print("The square root of 14.5 is approx. {}".format(pos))
