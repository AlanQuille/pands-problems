# This function implements "iterations" steps of the Newton-Raphson method
# for finding roots. In particular, it finds the roots of the equation
# x^2 - input, which is identical to asking what is the square 
# root of the input. The derivative of x^2 - input is 2x
def newton_root(input, iterations):
    # Rough guess of answer for Newton-Raphson
    init = input/4
    # This variable i is used in the while loop 
    i=0
    # This executes a while loop until i reaches iterations
    while i<iterations:
        # This is the formula for the Newton-Raphson method for finding
        # square roots
        init = init - ((init**2 - input)/(2*init))
        # Without this line of code, the loop would never reach iterations
        i = i +1
        
    return init
    




