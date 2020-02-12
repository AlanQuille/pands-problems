# Gets positive integer as input
any_pos_int = int(input("Please enter a positive integer: "))

# end programme if input is not a positive integer
if any_pos_int <= 0:
    # make user aware that incorrect data type has been
    # input
    print("The integer you have entered is not positive.")
else:
    # print out what the user input for any_pos_int
    # end =' ' ensures that it ends with a space
    # not newline
    print(any_pos_int, end=' ')
    # the while loop will end if any_pos_int is less than or equal to 1
    while(any_pos_int > 1):
        # if 2 divides into any_pos_int, divide it by two
        if(any_pos_int % 2 == 0):
            # This converts it to integer so it is not output with 
            # decimal places
            any_pos_int = int(any_pos_int/2)
        # else (it is odd) multiply by three and add one
        else:
            # This converts it to integer so it is not output with 
            # decimal places
            any_pos_int = int((any_pos_int * 3) + 1)
        # this prints any_pos_int and formats it as shown in
        # the example output
        print(any_pos_int, end=' ')
