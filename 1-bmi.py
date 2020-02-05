# weight in kg
weight = float(input("Enter weight: "))
# height in cm
height = float(input("Enter height: "))

# convert from cm to m
height = height/100

# get m^2 instead of m
height = height ** 2

# round to 2 decimal places
bmi = round(weight/height, 2)

# print to screen
print("BMI is", bmi)
