# sys module used here so that command line  
# arguments can be used in python script
import sys

# The number of 'e's is saved as variable
# ecount
ecount = 0

# This opens up the text file the user specifies
# in the command line after "python 7-es.py"
# for reading (indicated by 'r') as f
with open(sys.argv[1], 'r') as f:
    # This loops over each char in each line in f
    for line in f:
        for ch in line:
            # If the character is an 'e', increment ecount
            if(ch=='e'):
                ecount += 1

print(ecount)