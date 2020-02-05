# Get input and convert it to string
input_string = str(input("Please enter a sentence: "))

# Take the last letter, going to the first letter by
# by every second letter
output_string = input_string[-1:0:-2]

# Print the resulting string
print(output_string)
