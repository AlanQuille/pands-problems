# The number of 'e's is saved as variable
# ecount
ecount = 0

# This opens up the text file "e.txt"
# to read using the open function
with open("e.txt", 'r') as f:
    # This loops over each line in the text file
    for line in f:
        # This loops over each character in each line
        for ch in line:
            # If the character is an 'e', then ecount
            # is incremented
            if(ch=='e'):
                ecount += 1

print(ecount)