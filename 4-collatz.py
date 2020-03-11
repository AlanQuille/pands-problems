# Gets positive integer as input
any_pos_int = int(input("Please enter a positive integer: "))

# end programme if input is not a positive integer
if any_pos_int <= 0:
    print("The integer you have entered is not positive.")
else:
    print(any_pos_int, end=' ')
    # the while loop will end if any_pos_int is less than or equal to 1
    while(any_pos_int > 1):
        # if even, divide any_pos_int by two 
        if(any_pos_int % 2 == 0):
            any_pos_int = int(any_pos_int/2)
        # else (it is odd) multiply by three and add one
        else:
            any_pos_int = int((any_pos_int * 3) + 1)
            
        # print any_pos_int to screen
        # with blank space instead of newline.
        print(any_pos_int, end=' ')
