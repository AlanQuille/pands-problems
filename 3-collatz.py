# Gets positive integer as input
any_pos_int = int(input("Please enter a positive integer: "))

# end programme if input is not a positive integer
if any_pos_int <= 0:
    # make user aware that incorrect data type has been
    # input
    print("The integer you have entered is not positive.")
else:
    # the while loop will end if any_pos_int is less than or equal to 1
    while(any_pos_int > 1):
        # this prints any_pos_int and formats it as shown in
        # the example output
        print(any_pos_int, end=' ')
        # if 2 divides into any_pos_int, divide it by two
        if(any_pos_int % 2 == 0):
            # also converts it to integer so it is not float
            any_pos_int = int(any_pos_int/2)
            # else (it is odd) multiply by three and add one
        else:
            # also converts it to  integer so it is not a float
            any_pos_int = int((any_pos_int * 3) + 1)
